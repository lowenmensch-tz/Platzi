"""
    @author kenneth.cruz@unah.hn
    @version 0.1.0
    @date 2021/05/20
"""
import json

DATA = list( json.load( open("./Files/data.json", "r") ).values() )

def run():
    
    all_python_devs = [ worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_worker = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    adults = list(
        map(
            lambda worker: worker['name'], 
            filter(lambda worker: worker['age'] > 18, DATA))
    )
    #old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_people = list(map(lambda worker: {**worker, **{'old': worker['age'] > 70}} , DATA))

    print( old_people )


#Entry point
if __name__ == "__main__":
    run()
    #print( DATA )