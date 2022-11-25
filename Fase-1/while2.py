frase = 'O python é muito legal e divertido'

x = 0
newqnt = 0
letra = ''
while x < len(frase):
    qnt = frase.lower().count(frase[x])
    if qnt > newqnt and not frase[x] == ' ':
        newqnt = qnt
        letra = frase[x]
    x += 1

print(f'A letra que mais apareceu foi "{letra}", ela apareceu {newqnt} vezes!')
    