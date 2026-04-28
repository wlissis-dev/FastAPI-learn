from pydantic import BaseModel
from typing import List, Literal

from pydantic import Field

#Classe base
class PokemonBase(BaseModel):
    # id: int
    # nome: str
    # tipo: List[str]
    id: int = Field(..., description="O número da Pokedex")
    nome: str = Field(..., description="Nome do Pokémon")
    tipo: List[str] = Field(..., description="Ex: ['Fogo', 'Voador']")
    nivel: int = Field(default=1, ge=1, le=100, description="Nível entre 1 e 100")

    # esse campo precisa ser um Literal.
    # Isso garante que o valor seja fixo e imutável 
    # (ex: "é True" ou "é False"), permitindo que o Pydantic saiba 
    # exatamente qual classe escolher apenas olhando para esse valor.
    is_lendario: Literal[False] = False

# Classe específica usando Herança
class PokemonLendario(PokemonBase):
    regiao_origem: str

    # esse campo precisa ser um Literal.
    # Isso garante que o valor seja fixo e imutável 
    # (ex: "é True" ou "é False"), permitindo que o Pydantic saiba 
    # exatamente qual classe escolher apenas olhando para esse valor.
    is_lendario: Literal[True] = True