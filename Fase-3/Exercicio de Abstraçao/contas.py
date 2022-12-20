from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero: int, agencia: int) -> None:
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0

    def depositar(self, value: float) -> bool:
        if value <= 0:
            return False

        self.saldo += value
        return True

    @abstractmethod
    def sacar(self, value: float) -> bool: ...

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.numero!r}'
        return f'{class_name}({attrs})'


class ContaCorrente(Conta):
    def __init__(self, numero: int, agencia: int, limite: float = 0) -> None:
        super().__init__(numero, agencia)
        if limite > 0:
            self._limite = -limite
        else:
            self._limite = 0

    def sacar(self, value: float):
        if (self.saldo - value) < self._limite:
            return False

        self.saldo -= value
        return True

    def set_limite(self, value: float) -> None:
        if value > 0:
            self._limite = -value


class ContaPoupanca(Conta):

    def sacar(self, value: float):
        if value > self.saldo or value <= 0:
            return False

        self.saldo -= value
        return True
