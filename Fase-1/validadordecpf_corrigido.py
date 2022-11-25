cpf = ("".join((input('Digite: ').replace('-', '.')).split('.')))
teste_cpf = cpf[:9]
k = 0
while k < 2:
    qnt = len(teste_cpf)
    z = 0
    for x, y in enumerate(teste_cpf, -(qnt+1)):
        x *= -1
        t = x * int(y)
        z += t
        if x == 2:
            if qnt == 9:
                n1 = 0 if ((z % 11) < 2) else (11 - (z % 11))
                teste_cpf += str(n1)
            elif qnt == 10:
                n2 = 0 if ((z % 11) < 2) else (11 - (z % 11))
                teste_cpf += str(n2)
            k += 1
            break

validador = cpf[0] * len(cpf) # Impedi CPF com numeros sequenciais

print('CPF VALIDO' if teste_cpf == cpf and teste_cpf != validador else 'CPF INVALIDO')