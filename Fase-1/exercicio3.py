user = input('Digite seu nome: ')
contuser = len(user)
TESTE_NOME = 'seu nome é grande' if contuser > 6 else ('seu nome é pequeno' if contuser < 5 else 'Seu nome é Normal')
print(TESTE_NOME)