from contas import ContaPoupanca, ContaCorrente
from clientes import Cliente


class Banco:
    def __init__(self, agencia):
        self.agencia = agencia
        self.clientes = []
        self.contas = []

    def checar_conta(self, cliente: Cliente) -> bool:
        if cliente.conta is None:
            return True
        return False

    def vincular_cliente(self, cliente: Cliente) -> bool:
        if self.checar_conta(cliente):
            return False
        elif cliente.conta.agencia == self.agencia:
            self.clientes.append(cliente)
            self.contas.append(cliente.conta)
            return True
        return False

    def saque(self, cliente: Cliente, value: int):
        if self.checar_conta(cliente):
            return False
        elif cliente.conta not in self.contas:
            return False

        for c in self.clientes:
            if c == cliente:
                return cliente.conta.sacar(value)

    def deposito(self, cliente: Cliente, value: int):
        if self.checar_conta(cliente):
            return False
        elif cliente.conta not in self.contas:
            return False

        for c in self.clientes:
            if c == cliente:
                return cliente.conta.depositar(value)

    def saldo_cliente(self, cliente: Cliente) -> str:
        if self.checar_conta(cliente):
            return 'O Cliente não possui conta cadastrada.'
        return f'O saldo é: {cliente.conta._saldo:.2f}'


banco1 = Banco(500)

conta1 = ContaCorrente(agencia=500, numero=264849)
conta1.set_limite(500)
conta2 = ContaPoupanca(agencia=900, numero=4748)

cliente1 = Cliente('Richard', 22)
cliente1.conta = conta1
cliente2 = Cliente('Sara', 22)
cliente2.conta = conta2


def check_add_cliente(banco: Banco, cliente: Cliente):
    if banco.vincular_cliente(cliente=cliente):
        print('Cliente adicionado ao Banco')
    else:
        print('Cliente não pertence a esse Banco')


def sacar(banco: Banco, cliente: Cliente, value: int):
    if banco.saque(cliente=cliente, value=value):
        print('Saque realizado com sucesso')
    else:
        print('Erro no saque!')


def depositar(banco: Banco, cliente: Cliente, value: int):
    if banco.deposito(cliente=cliente, value=value):
        print('Deposito realizado com sucesso')
    else:
        print('Erro no deposito!')


def saldo(banco: Banco, cliente: Cliente):
    print(banco.saldo_cliente(cliente))


if __name__ == '__main__':
    check_add_cliente(banco1, cliente1)
    check_add_cliente(banco1, cliente2)
    print()
    depositar(banco1, cliente1, 20)
    depositar(banco1, cliente2, 202)
    print()
    sacar(banco1, cliente1, 260)
    sacar(banco1, cliente2, 20)
    print()
    saldo(banco1, cliente1)
    saldo(banco1, cliente2)
