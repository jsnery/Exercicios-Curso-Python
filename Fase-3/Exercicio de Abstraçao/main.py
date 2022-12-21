from contas import ContaPoupanca, ContaCorrente, Conta
from clientes import Cliente


class Banco:
    def __init__(
        self,
        nome: str,
        agencias: list[int] | None = None,
        conta: list[Conta] | None = None,
        clientes: list[Cliente] | None = None
    ):
        self.nome = nome
        self.agencias = agencias or []
        self.contas = conta or []
        self._clientes = []
        self.clientes = clientes or []

    @property
    def clientes(self) -> list:
        return self._clientes

    @clientes.setter
    def clientes(self, clientes):
        for c in clientes:
            if c.conta is None:
                self._clientes.append(c)
                continue
            if c.conta.agencia in self.agencias:
                self._clientes.append(c)

    def _altenticar(self, cliente: Cliente):
        if cliente in self.clientes:
            if cliente.conta is None:
                cliente.token = False
                return
            if cliente.conta.agencia in self.agencias:
                if cliente.conta in self.contas:  # type: ignore
                    cliente.token = True
                    return
            cliente.token = False

    def sacar(self, cliente: Cliente, valor: int | float):
        self._altenticar(cliente)
        if not cliente.token:
            return 'Saque não realizado!'

        if cliente.conta._sacar(valor):   # type: ignore
            cliente.token = False
            return 'Saque Realizado com sucesso'
        cliente.token = False
        return 'Saque não finalizado'

    def depositar(self, cliente: Cliente, valor: int | float):
        self._altenticar(cliente)
        if not cliente.token:
            return 'Deposito não realizado!'

        if cliente.conta._depositar(valor):   # type: ignore
            cliente.token = False
            return 'Deposito Realizado com sucesso'
        cliente.token = False
        return 'Deposito não finalizado'


cliente1 = Cliente('Richard', 22)
cliente2 = Cliente('Sara', 22)
conta1 = ContaCorrente(26873483, 500, 1000)
conta2 = ContaPoupanca(52515, 240)
cliente1.conta = conta1
cliente2.conta = conta2


x = Banco('Bradesco')
x.agencias = [500]
x.agencias.append(240)
x.clientes = [cliente1, cliente2]
x.contas = [conta1, conta2]

print(*x.clientes, sep='\n')
print()
print(*x.contas, sep='\n')
print()
x.depositar(cliente1, 49951)
print('Depositando')
x.depositar(cliente2, 47783)
print()
print(*x.contas, sep='\n')
print()
x.sacar(cliente1, 50021)
print('Sacando')
x.sacar(cliente2, 2426)
print()
print(*x.contas, sep='\n')
print()
