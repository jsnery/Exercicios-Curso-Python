class Fabricante():
    def __init__(self, nome):
        self.nome = nome
        self._carros = []
    
    @property
    def carros(self):
        return self._carros
    
    @carros.setter
    def carros(self, value):
        self._carros.append(Carro(value, self.nome))
        
    @property
    def listar(self):
        for carro in self._carros:
            print(f"Fabrincante: {carro.fabricante}\nModelo: {carro.modelo}\nMotor: {carro.motor.nome}")
            print()


class Carro:
    def __init__(self, modelo, fabricante):
        self.fabricante = fabricante
        self.modelo = modelo
        self._motor = 'Sem Motor'
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, value):
        self._motor = value
              

class Motor:
    def __init__(self, nome):
        self.nome = nome
        
        
        
ford = Fabricante('Ford')

ford.carros = 'Focus'
ford.carros = 'Fiesta'
ford.carros = 'KA'

v8 = Motor('V8 Turbo')

ford.carros[0].motor = v8
ford.carros[1].motor = v8
ford.carros[2].motor = v8


ford.listar

