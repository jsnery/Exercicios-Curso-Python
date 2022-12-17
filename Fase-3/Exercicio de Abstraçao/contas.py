from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, numero, agencia):
        self.agencia = agencia
        self.numero = numero
        self._saldo = 0

    def Depositar(self, value) -> bool:
        if value <= 0:
            return False
        
        self._saldo += value
        return True

    @abstractmethod
    def Sacar(self) -> bool:...


class ContaCorrente(Conta):

    def Sacar(self, value):
        if (self._saldo - value) <= -200:
            return False
        
        self._saldo -= value
        return True
    
    
class ContaPoupanca(Conta):

    def Sacar(self, value):
        if value > self._saldo or value <= 0:
            return False
        
        self._saldo -= value
        return True