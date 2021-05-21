"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
"""


def run():
    try: 
        number = int(input("Ingrese un número para encontrar sus divisores: "))
        if number < 0: 
            raise NameError("Números negativos")
        print([x for x in range(1, number + 1) if number % x == 0])
    except ValueError as ve: 
        print("Error al ingresar número: {}".format(ve))
    except NameError as ne: 
        print("Error al ingresar número: {}".format(ne))
    

if __name__ == "__main__": 
    run()