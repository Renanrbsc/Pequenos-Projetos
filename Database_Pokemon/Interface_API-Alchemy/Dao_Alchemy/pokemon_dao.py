from Dao_Alchemy.base_dao import BaseDao
from Model_Alchemy.pokemon_model import PokemonModel


class PokemonDao(BaseDao):

    def get_all(self):
        pokemon_all = super().get(PokemonModel)
        list_pokemon = []
        for pokemon in pokemon_all:
            list_pokemon.append(self.dict(pokemon))
        return list_pokemon

    def get_by_id(self, id):
        pokemon = super().get(PokemonModel, id)
        return self.dict(pokemon)

    def insert(self, Pokemon: PokemonModel):
        return super().insert(Pokemon)

    def update(self, Pokemon: PokemonModel):
        id = Pokemon.id
        return super().update(Pokemon, id)

    def remove(self, id):
        search = super().get(PokemonModel, id)
        return super().remove(search, id)

    def dict(self, pokemon):
        poke = {"codigo": pokemon.id, "nome": pokemon.nome, "tipo": pokemon.tipo, "altura": pokemon.altura,
                "peso": pokemon.peso, "categoria": pokemon.categoria, "habilidade": pokemon.habilidade,
                "habilidade2": pokemon.habilidade2, "fraqueza": pokemon.fraqueza,
                "fraqueza2": pokemon.fraqueza2, "descricao": pokemon.descricao
                }
        return poke