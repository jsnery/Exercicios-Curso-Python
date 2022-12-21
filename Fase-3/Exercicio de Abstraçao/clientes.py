from contas import Conta


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}({attrs})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None
        self.token = False

    # @property
    # def conta(self):
    #     return self._conta

    # @conta.setter
    # def conta(self, conta):
    #     self._conta = conta
