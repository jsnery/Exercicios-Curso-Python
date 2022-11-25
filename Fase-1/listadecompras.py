import os

def clear():
    os.system("cls")

def listaprodutos(lista):
    print('Lista de Produtos:')
    for indice, item in enumerate(lista, 1):
        print(indice, item)

lista = []
OPCOES = 'IALS'
clear()

produto = input('Adicione o primeiro item: ').upper()
lista.append(produto)
clear()
while True:
    while True:
        op = input(f'Menu:\n\n[i]nseir | [a]pagar | [l]istar | [s]air\n\nDigite aqui: ').upper() 

        if len(op) > 1 or not op in OPCOES:
            clear()
            print('Escolha entre as opções abaixo!\n')
        else:
            break

    if op == 'A':
        clear()
        while True:
            try:
                op2 = int(input("Escolha\n\n1) Deseja escrever o item\n2) Deseja apagar o ultimo\n\nDigite aqui: "))
            except:
                clear()
                print('Digite apenas uma das opções abaixo!\n')
                continue

            if op2 <=2 and op2 > 0:
                break
            else:
                clear()
                print('Escolha entre as opções abaixo!\n')
        
        if op2 == 1:
            clear()
            while True:
                try:
                    lista.pop(lista.index(input('Digite o Nome do Item: ').upper()))
                    clear()
                    break
                except:
                    clear()
                    print('Item Não encontrado\n')
                    while True:
                        try:
                            op3 = int(input("Escolha\n\n1) Continuar\n2) Sair\n\nDigite aqui: "))
                        except:
                            clear()
                            print('Digite apenas uma das opções abaixo!\n')
                            continue

                        if op3 <=2 and op3 > 0:
                            break
                        else:
                            clear()
                            print('Escolha entre as opções abaixo!\n')
                    if op3 == 1:
                        clear()
                        continue
                    else:
                        os._exit(0)

        else:
            clear()
            lista.pop()

    elif op == 'I':
        clear()
        produto = input('Insira o item: ').upper()
        lista.append(produto)
        clear()
        
    elif op == 'L':
        clear()
        listaprodutos(lista)
        print()

    else:
        os._exit(0)