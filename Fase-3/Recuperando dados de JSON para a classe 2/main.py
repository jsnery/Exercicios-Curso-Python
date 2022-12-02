import json
from os import path, system
from itertools import count

class Pessoa:
    def __init__(self, nome, sobrenome, idade, peso, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imc(self):
        return (self.peso / (self.altura ** 2))

contador = count(1)
DIR = path.dirname(__file__)
JSONNAME = path.join(DIR, 'pessoas.json')



with open(JSONNAME, 'r') as file:
    dados = json.load(file)

index = {f'pessoa{next(contador)}': Pessoa(**p) for p in dados}

print(index)




