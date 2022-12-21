from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero: int, agencia: int) -> None:
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0.0

    def _depositar(self, value: float) -> bool:
        if value <= 0:
            return False

        self.saldo += value
        return True

    @abstractmethod
    def _sacar(self, value: float) -> bool: ...

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'Agência: {self.agencia!r},'\
                f' Conta: {self.numero!r}, Saldo: {self.saldo!r}'
        return f'{class_name}({attrs})'


class ContaCorrente(Conta):
    def __init__(self, numero: int, agencia: int, limite: int | float = 0):
        super().__init__(numero, agencia)
        if limite > 0:
            self._limite = -limite
        else:
            self._limite = 0

    def _sacar(self, value: int | float):
        if (self.saldo - value) < self._limite:
            return False

        self.saldo -= value
        return True

    def set_limite(self, value: int | float) -> None:
        if value > 0:
            self._limite = -value


class ContaPoupanca(Conta):

    def _sacar(self, value: float):
        if value > self.saldo or value <= 0:
            return False

        self.saldo -= value
        return True
