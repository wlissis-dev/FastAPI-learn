from fastapi import FastAPI, HTTPException
from .models import PokemonBase, PokemonLendario
from typing import List

from typing import Union, Annotated
from pydantic import Field

app = FastAPI()

#Pokedex, banco de memória
pokedex_db: List[Union[PokemonBase, PokemonLendario]] = []

# O FastAPI usa o campo 'is_lendario' para decidir qual classe usar
PokemonUnion = Annotated[Union[PokemonLendario, PokemonBase], Field(discriminator='is_lendario')]

@app.post("/pokemons",status_code=201)
def cadastrar_pokemon(pokemon:PokemonUnion):
    pokedex_db.append(pokemon)
    return {"status": "Registrado", "tipo": pokemon.is_lendario}