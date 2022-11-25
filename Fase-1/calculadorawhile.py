import os
os.system('cls')
nvalidos = None
x = 0
newn1 = 0
newn2 = 0
print('Calculadora\n')
while x == 0:
    n1 = input('Digite o primeiro numero: ').replace(',', '.')
    operador = input('Digite a operação: (+ - * /) ')
    n2 = input('Digite o segundo numero: ').replace(',', '.')
    resultado = 0

    try:
        try:
            newn1 = int(n1)
            newn2 = int(n2)
            nvalidos = True
        except ValueError:
            newn1 = float(n1)
            newn2 = float(n2)
            nvalidos = True
    except:
        nvalidos = None

    if nvalidos:
        if len(operador) > 1:
            os.system('cls')
            resultado = 'Digite apenas um operador!\n'
        elif operador == '+':
            resultado += (newn1 + newn2)
        elif operador == '-':
            resultado += (newn1 - newn2)
        elif operador == '*':
            resultado += (newn1 * newn2)
        elif operador == '/':
            resultado += (newn1 / newn2)
        else:
            resultado = 'Operador Invalido!'
    else:
        resultado = 'Digite Numeros validos'

    os.system('cls')
    print(resultado)

    sair = input('\nDeseja continuar? [s]im')
    COND1 = sair.lower().startswith('s')
    COND2 = sair.lower().endswith('m')
    x = 0 if COND1 or (COND1 and COND2) else 1
    os.system('cls')
    print('Calculadora\n')

os.system('cls')