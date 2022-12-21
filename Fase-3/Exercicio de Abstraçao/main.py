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
        self.clientes = clientes or []

    @property
    def agencias(self) -> list:
        return self._agencia

    @agencias.setter
    def agencias(self, agencias: list):
        self._agencia = agencias

    @property
    def contas(self) -> list[Conta] | None:
        return self._contas

    @contas.setter
    def contas(self, conta):
        self._contas = conta

    @property
    def cliente(self) -> list:
        return self._cliente

    @cliente.setter
    def cliente(self, clientes):
        clientes_validos = []
        contas_validas = []
        for c in clientes:
            if c.conta is None:
                continue
            if c.conta.agencia in self.agencias:
                clientes_validos.append(c)
                contas_validas.append(c.conta)

        self._cliente = clientes_validos
        self._contas = contas_validas


x = Banco('Bradesco')
x.agencias = [500]
x.agencias.append(240)

cliente1 = Cliente('Richard', 22)
cliente2 = Cliente('Sara', 22)
conta1 = ContaCorrente(26873483, 500, 1000)
conta2 = ContaPoupanca(52515, 240)
cliente1.conta = conta1
cliente2.conta = conta2

x.cliente = [cliente1, cliente2]

print(x.cliente)
print(x.contas)
