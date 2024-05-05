from fastapi import FastAPI
from pokeapi import Pokemon

app = FastAPI()


@app.get('/pokemon/{name}')
def get_pokemon(name: str):
    poke = Pokemon(name)
    row = poke.show()
    return {'Dato': row}