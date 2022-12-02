import json
from os import path, system

class Pessoa:
    def __init__(self, nome, sobrenome, idade, peso, altura):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imc(self):
        return (self.peso / (self.altura ** 2))

people = {
    '1': Pessoa(nome='Richard', sobrenome='Neri', idade=22, peso=78, altura=1.76),
    '2': Pessoa(nome='Sara', sobrenome='Gomes', idade=22, peso=56, altura=1.64),
    '3': Pessoa(nome='Joelma', sobrenome='Santos', idade=43, peso=60, altura=1.60)
}


index = None
while True:
    system('clear')
    print('Tela de salvamento\n' if index is None else 'Escolha uma opção valida!\n')
    index = input('Digite o numero da pessoa para salvar: ')
    if index not in people.keys():
        continue
    break

nomePessoa = people[index].nome
dictPessoa = vars(people[index])

DIR = path.dirname(__file__)
JSONNAME = path.join(DIR, f'{nomePessoa}.json')

with open(JSONNAME, 'w') as file:
    json.dump(dictPessoa, file, indent=2)

