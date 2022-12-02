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


p1 = Pessoa(nome='Richard', sobrenome='Neri', idade=22, peso=78, altura=1.76)
p2 = Pessoa(nome='Sara', sobrenome='Gomes', idade=22, peso=56, altura=1.64)
p3 = Pessoa(nome='Joelma', sobrenome='Santos', idade=43, peso=60, altura=1.60)

pessoas = [vars(p1), vars(p2), vars(p3)]

DIR = path.dirname(__file__)
JSONNAME = path.join(DIR, 'pessoas.json')

if __name__ == '__main__': # assim ele só será executado quando esse for o principal Kkkkkk
    def salvar():
        with open(JSONNAME, 'w') as file:
            json.dump(pessoas, file, indent=2)

