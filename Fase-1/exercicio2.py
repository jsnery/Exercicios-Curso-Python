hora = input('Que horas são? ')
newhora = hora[:2]
teste_hora = int(newhora) > 23 or int(newhora) < 0 if newhora.isdigit() else not newhora.isdigit()

while teste_hora:
    hora = input('Não entendi\n\nQue horas são? ')

hora_convertida = int(newhora)
SAUDACAO = 'Bom Dia' if hora_convertida <= 11 else ('Boa Tarde' if hora_convertida <= 17 else 'Boa Noite')

print(SAUDACAO)