"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
"""

"""
    Dibuja el muñeco del 
    ahorcado por consola 
"""
class Draw: 

    def __init__(self) -> None:

        self.h1 = [" "*2 + "|" + " "*3 +"|"+" "*2 ]
        t1 = [" "*6+"|"+" "*2]
        
        self.hangman = [
            self.h1, t1, t1,
            t1, t1, t1,
            ["="*9]
        ]


    """
        Dibuja el muñeco del ahorcado
    """
    def draw(self, hangman):

        return "".join( [ "".join(row) + '\n' for row in hangman] ) + '\n'


    def draw_process(self, content: list, index) -> None:

        self.hangman[index] = content
        return self.draw(self.hangman)


    """
        Depende de las vidas restantes del 
        jugador así irá avanzando el dibujo
    """
    def process(self, lives):

        if lives == 4:
            return self.draw(self.hangman)
        elif lives == 3: 
            return self.draw_process(self.h1, 1) 
        elif lives == 2:
            return self.draw_process([" "*2 + "O" + " "*3 +"|"+" "*2 ], 2)
        elif lives == 1:
            return self.draw_process([" " + "/|\\" + " "*2 +"|"+" "*2], 3)
        else:
            return self.draw_process([" " + "/ \\" + " "*2 +"|"+" "*2], 4)