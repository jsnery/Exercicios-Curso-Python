nome = input('Qual o seu nome? ')
nomep = input('Qual o seu nome de preferencia? ')
sexo = input('Qual o seu sexo biológico? ')  
idade = input('Qual a sua idade? ')
altura = input('Qual a sua altura? ')
peso = input('Qual o seu peso? ')
print('')

idade = int(idade)
altura = float(altura)
peso = float(peso)

imc = peso / (altura ** 2)

print('Ficha do Paciênte\n ')
print('Nome:', nome)
print('Sexo:', sexo)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', peso)
print('')
print(nomep, 'tem', idade, 'anos de idade e seu imc é', imc)
print('')

print(f'{nomep} tem {idade} anos de idae e seu imc é {imc}!') #f'string' utilizando {}
print('')

print(f'{nomep} tem {idade} anos de idae e seu imc é {imc:.2f}!') # :.2f ou seja 2 casas decimais
print('')

print('{} tem {} anos de idade e seu imc é {:.2f}!'.format(nomep, idade, imc)) #tem que seguir a ordem
print('')

print('{2} tem {0} anos de idade e seu imc é {1:.2f}!'.format(idade, imc, nomep)) #Marca asequencia e pode usar quando precisar
print('')

print('{n} tem {i} anos de idade e seu imc é {im:.2f}!'.format(n=nomep, i=idade, im=imc)) #tem que seguir a ordem