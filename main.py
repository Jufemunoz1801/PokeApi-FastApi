from fastapi import FastAPI# Import fastapi packages
from pokeapi import Pokemon# import the Pokemon class from pokeapi file

app = FastAPI()# object instantiation 


@app.get('/pokemon/{name}')# path definition using get method
def get_pokemon(name: str):
    poke = Pokemon(name)# call to the Pokemon class
    row = poke.show()# call the show method from pokemon class
    return {'Dato': row}# show the result