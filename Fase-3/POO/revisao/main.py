class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.__fabricante = None
        self.__motor = None
    
    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, value):
        self.__motor = value
    
    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
            
    def detalhar(self):
        modelo = self.nome
        fabricante = self.fabricante.nome
        motor = self.motor.nome
        print(f'Modelo: {modelo}\nFabricante: {fabricante}\nMotor: {motor}\n')
    
            
class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome
        
        
######## Motores
motor1 = Motor('v8 Turbo')
motor2 = Motor('1.0')
motor3 = Motor('2.0')

####### Fabricantes
fiat = Fabricante("Fiat")
ford = Fabricante("ford")


###### Palio
palio = Carro('Palio')
palio.fabricante = fiat
palio.motor = motor2
palio.detalhar()

##### Focus
focus = Carro('Focus')
focus.fabricante = ford
focus.motor = motor3
focus.detalhar()



