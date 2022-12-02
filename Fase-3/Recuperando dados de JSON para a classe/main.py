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


people = {}

DIR = path.dirname(__file__)
contador = count(1)


while True:
    arquivo = None
    dados = None
    while True:
        print('Tela de carregamento\n' if arquivo is None else 'Escolha uma arquivo valido!\n')
        arquivo = input('Digite o nome do arquivo JSON: ')

        JSONNAME = path.join(DIR, f'{arquivo}.json')
        if not path.isfile(JSONNAME):
            system('clear')
            continue
        break

    with open(JSONNAME, 'r') as file:
        dados = json.load(file)

    people.setdefault(f'pessoa{next(contador)}', Pessoa(**dados))

    system('clear')
    print(people, '\n')