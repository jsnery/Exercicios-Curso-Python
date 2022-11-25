import sys 

# IMPAR ou PAR
# Variaveis
number = input('Digite um numero Inteiro: ')
numberdic = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Teste de variaveis // Processamento
if not number.isdigit():
  print('Isso não é um número inteiro!')
  sys.exit()
else:
  number = int(number)
  result = number % 2
  # Resultado // Processamento
  
  if number == 0:
    print(f'{number} é neutro')
  elif result == 0:
    print(f'{number} é PAR')
  else:
    print(f'{number} é IMPAR')