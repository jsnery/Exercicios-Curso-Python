from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self._idade = idade

    @property
    @abstractmethod
    def nome(self):...


    @property
    @abstractmethod
    def idade(self):...


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, conta):
        super().__init__(nome, idade, cpf)
        self.conta = conta

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    