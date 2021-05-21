"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/21
"""

def read():
    
    number = list( 
        map(
            lambda x: int(x.strip()), 
            open("./Files/numbers.txt", "r", encoding='utf-8').read().split("\n")
        )
     ) 


def write():
    
    name = ["Facundo", "Miguel", "Pepe", "Christian", "Rocío"]
    with open("./Files/names.txt", "a", encoding='utf-8') as f: 
        for _ in name: 
            f.write(_ + "\n")
        f.close()

def run():
    read()
    write()


if __name__ == "__main__":
    run()   