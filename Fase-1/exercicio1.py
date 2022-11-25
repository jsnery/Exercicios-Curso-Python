# IMPAR ou PAR
numero = input('Digite um numero Inteiro: ')

while not numero.isdigit() or numero == '0':
	print('Numero Invalido\n')
	numero = input('Digite um numero Inteiro: ')

EPAR = int(numero) % 2 == 0

print(f'O NUMERO {numero} É PAR' if EPAR else f'O NUMERO {numero} ÉIMPAR')