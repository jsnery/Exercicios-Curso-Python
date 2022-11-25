from random import randint

cpf = str(randint(100000000, 999999999))
k = 0
while k < 2:
    qnt = len(cpf)
    z = 0
    for x, y in enumerate(cpf, -(qnt+1)):
        x *= -1
        t = x * int(y)
        z += t
        if x == 2:
            if qnt == 9:
                n1 = 0 if ((z % 11) < 2) else (11 - (z % 11))
                cpf += str(n1)
            elif qnt == 10:
                n2 = 0 if ((z % 11) < 2) else (11 - (z % 11))
                cpf += str(n2)
            k += 1
            break

cpf = list(cpf)
cpf = "".join(cpf[0:3]) + "." + "".join(cpf[3:6]) + "." + "".join(cpf[6:9]) + "-" + "".join(cpf[9:])

print('CPF GERADO: ', cpf)