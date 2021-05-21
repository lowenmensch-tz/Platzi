"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
"""

import json
import re
import os
from random import randint

"""
    Juego: El ahorcado
"""
class Game: 

    #♡
    def __init__(self) -> None:
        
        self.message = [
            "Bienvenido: Juego El ahorcado", 
            "\n\nIngrese la dificultad del juego:\n\n[1] Fácil\n[2] Intermedio\n[3] Difícil\nPresione cualquier tecla para salir.\n\n",
            "\nVidas: {}\nComplete la palabra oculta:\n\n\t\t{}\t\t\n\nTiene {} letras ocultas", 
            "\n\nIngrese una letra: ",
            "\nPresione ENTER\n\n", 
            "Felicidades, ha adivinado la palabra: {}", 
            "*", 
            "♥", 
            "Ha perdido"
        ]

        self.answer = []
        self.data = json.load( open("data.json", "r") ).values()

    
    """
        Escoge una palabra según la dificultad (1 fácil, 2 intermedio, 3 difícil)
        en base al archivo JSON que contiene las palabras que se utilizan en el juego
    """
    def process_data(self, difficulty: int) -> dict: 
        
        hangman_word = list(
                filter(
                    lambda x: x['difficulty'] == difficulty, 
                    self.data
            )
        )

        return (hangman_word[randint(0, len(hangman_word)-1)])

    
    """
        Pistas sobre la palabra a encontrar
    """
    def clues(self, word: str) -> None: 
        
        count_word = len(
            [
                x for x in word if re.search(r"[AEIOUÁÉÍÓÚÜ]")
            ]
        )

        print("La palabra tiene {} vocales.".format(count_word))

    
    """
        Comparación de la palabra escogida por el juego con respecto 
        a la respuesta ingresadas por el usuario.
        Retorna una lista con los índices de las coincidencias
    """
    def compare(self, answer_user: str, hangman_word: str) -> dict:
        
        return {str(i):hangman_word[i] for i in range(len(hangman_word)) if answer_user == hangman_word[i]}


    """
        Formación de la palabra oculta con las respuestas 
        correctas del usuario
    """
    def process_answer(self, dict_answer_index: dict, new_hangman_word: str) -> str: 
        
        new_word = [ x for x in new_hangman_word]

        for k, v in dict_answer_index.items(): 
            new_word[int(k)] = dict_answer_index[k]

        return "".join(new_word)


    """
        Mensaje de bienvenida o mensaje de celebración
    """
    def welcome_message(self, message: str)-> str: 
        
        decorative ='\n' + '*'+self.message[6]*len(message)+'*'+ '\n'
        return  decorative+'*'+message+'*'+decorative


    """
        Sistema de puntuaciones
    """
    def cls(self, message) -> None:
        
        os.system("clear") # Comando en Windows: cls
        print(message)
        

    """
        Pantalla de inicio
    """
    def input_game(self): 

        try: 

            difficulty = int(input( self.welcome_message(self.message[0]) + self.message[1]))
            hangman_word = (self.process_data(difficulty)['word']).upper()
            hidden_word = "".join(["_" for _ in hangman_word])
            lives = 4

            while(True): 
                
                hidden_letter = len([x for x in hidden_word if x == '_'])

                #Ganó
                if hidden_letter == 0: 
                    self.cls( self.welcome_message( self.message[5].format( hangman_word ))  )
                    break

                self.cls( self.message[2].format( self.message[7]*lives,  hidden_word, hidden_letter) )
                self.answer.append( (input( self.message[3] )).upper().strip() )

                #Letra repetida
                if len([x for x, word in enumerate( self.answer ) if word == self.answer[-1]]) != 1:
                    self.cls("Está letra ya fue ingresada: {}".format( self.answer.pop() ))
                    print(input(self.message[4]))
                else: 
                    dict_answer_index = self.compare(self.answer[-1], hangman_word)

                    if dict_answer_index: 
                        hidden_word = self.process_answer(dict_answer_index, hidden_word)
                    else: 
                        lives -= 1    

                #Perdió
                if lives == 0: 
                    self.cls( self.welcome_message(self.message[8]) )
                    break

        except ValueError as ve: 
            self.cls( "Bye".format(ve) )
            
        except KeyError as ke: 
            print( "El documento json está vacío".format(ke) )