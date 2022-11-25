def teste(u):
    x = (u % 11)
    if x < 2:
        valor = 0
    else:
        valor = 11 - (u % 11)
    return valor

def calculo(lista, qnt):
    z = 0
    for x, i in enumerate(lista, -(qnt+1)):
        x *= -1
        i = int(i)
        z += (i*x)
        if x == 2:
            break
    return z

cpf = ("".join((input('Digite: ').replace('-', '.')).split('.')))
validador = cpf
cpf = cpf[:9]

n1 = str(teste(calculo(cpf, len(cpf))))
cpf += n1
n2 = str(teste(calculo(cpf, len(cpf))))
cpf += n2

print('\nCPF Valido' if (cpf == validador) else '\nCPF Invalido')