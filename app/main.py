from fastapi import FastAPI, HTTPException, status
from .models import PokemonBase, PokemonLendario
from typing import List

from typing import Union, Annotated
from pydantic import Field

app = FastAPI()

#Pokedex, banco de memória
pokedex_db: List[Union[PokemonBase, PokemonLendario]] = []

# O FastAPI usa o campo 'is_lendario' para decidir qual classe usar
PokemonUnion = Annotated[Union[PokemonLendario, PokemonBase], Field(discriminator='is_lendario')]

@app.post("/pokemons",status_code=status.HTTP_201_CREATED)
def cadastrar_pokemon(pokemon:PokemonUnion):
    """
    adiciona um pokemon 
    """
    for p in pokedex_db:
        if p.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Este ID já existe na Pokedex!"
            )
    pokedex_db.append(pokemon)
    return {"message": "Pokémon cadastrado com sucesso", "pokemon": pokemon}

@app.get("/pokemons", status_code=status.HTTP_200_OK)
def listar_pokemons():
    """
    Retorna uma lista contendo todos os Pokémons cadastrados na Pokedex.
    """
    return pokedex_db


@app.get("/pokemons/{pokemon_id}", status_code=status.HTTP_200_OK)
def buscar_pokemon(pokemon_id: int):
    for pokemon in pokedex_db:
        if pokemon.id == pokemon_id:
            return pokemon
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Pokémon com ID {pokemon_id} não encontrado"
    )
   