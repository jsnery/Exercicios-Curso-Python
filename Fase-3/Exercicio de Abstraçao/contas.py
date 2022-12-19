from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, agencia):
        self.agencia = agencia
        self.numero = numero
        self._saldo = 0

    def depositar(self, value) -> bool:
        if value <= 0:
            return False
        
        self._saldo += value
        return True

    @abstractmethod
    def sacar(self) -> bool:...


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, limite=0):
        super().__init__(numero, agencia)
        if limite > 0:
            self._limite = -limite
        else:
            self._limite = 0

    def sacar(self, value):
        if (self._saldo - value) < self._limite:
            return False
        
        self._saldo -= value
        return True
    
    def set_limite(self, value):
        if value > 0:
            self._limite = -value
        
    
    
class ContaPoupanca(Conta):

    def sacar(self, value):
        if value > self._saldo or value <= 0:
            return False
        
        self._saldo -= value
        return True