import string, os

def clear():
    os.system('cls')

palavra = 'abacate'
dados = list(len(palavra) * '_')
palpite = None
resposta = None
tentativas = len(palavra)
clear()
print('Caça palavras:\n')
while True:
    if tentativas == 0:
        clear()
        print('VOCÊ PERDEU!\n')
        print(f'A palavra era {palavra}\n')
        break

    palpite = input('Digite uma letra: ')
    validadedopalpite = palpite.isnumeric() or palpite in string.punctuation or len(palpite) > 1 or palpite == " "

    if validadedopalpite:
        clear()
        print('Digite somente uma letra!\n')
        continue
    elif palpite in palavra:  
        for indice, letra in enumerate(palavra):
            if palpite == letra:
                dados[indice] = palavra[indice]
    else:
        tentativas -= 1
        clear()
        print(f'Você errou, restam {tentativas} chances!\n')
        continue

    resposta = "".join(dados)
    if resposta == palavra:
        clear()
        print('VOCÊ GANHOU!\n')
        print(f'A palavra é {resposta}\n')
        break
    
    clear()
    print('Caça palavras:\n')
    print(f'{resposta}\n')