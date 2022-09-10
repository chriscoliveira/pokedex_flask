#  https://pokeapi.co/api/v2/pokemon/

import requests


class Pokemon:

    def __init__(self, nome, foto, foto1, tipo, movimentos, peso, formas, id, habilidades, local, status):
        self.nome = nome
        self.foto1 = foto1
        self.foto = foto
        self.tipo = tipo
        self.movimentos = movimentos
        self.peso = peso
        self.idade = id
        self.status = status
        self.formas = formas
        self.habilidades = habilidades
        self.local = local
