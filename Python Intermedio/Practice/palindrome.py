"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
"""

def run():
    word = (input("Escriba una palabra: ")).replace(" ", "").lower()
    return False if word[::-1] != word or len(word) == 0 else True


if __name__ == "__main__": 
    print( run() )
