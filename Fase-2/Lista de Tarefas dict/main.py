from copy import deepcopy
from os import system, path
import json

DIR = path.dirname(__file__)

def clear():
    system('clear')
       
def novasTarefas(lista=None):
    clear()
    def locaisTarefas(n, t=None, index=1):
        clear()
        if t == None:
            t = {}
        addTarefa = input(f"Digite a {index}º tarefa: ")
        t = {**t, f'{index}': addTarefa}
        return t if index == n else locaisTarefas(n, t, index+1)
    
    opcoes = None
    while True:
        print('Apenas numeros Inteiros\n' if opcoes is not None else 'Adicionando Tarefas\n')
        opcoes = input('Quantidade de tarefas: ')
        if opcoes.isdecimal():
            qnt = int(opcoes)
            break
        clear()

    if lista is None:
        return locaisTarefas(qnt)
    return locaisTarefas(qnt, t=lista)

def exportTarefas(lista, listaName):
    JSONNAME = path.join(DIR, f'{listaName}.json')
    TXTNAME = path.join(DIR, f'{listaName}.txt')
    
    with open(JSONNAME, 'w') as jasonFile:
        json.dump(lista, jasonFile, indent=2)    
        
    with open(TXTNAME, 'w') as file:
        file.write('Lista de Tarefas\n\n')
        for i, tarefa in enumerate(lista.values(), 1):
            file.write(f'{i}º - {tarefa}\n')
            
def importTarefas(listaName):
    JSONNAME = path.join(DIR, f'{listaName}.json')
    
    with open(JSONNAME, 'r') as jasonFile:
        return json.load(jasonFile)    

def popTarefas(numero):
    global listaTarefa
    if numero.isdecimal():
        if int(numero) <= len(listaTarefa):
            listaTarefa.pop(numero)
            listaTarefa = {f'{i}': item for i, item in enumerate(listaTarefa.values(), 1)}
            return 
        print('O item não está presente nessa lista!')
        return
    print("Opção invalida!")
    return

backupListaTarefas = None
opcoes = None
menu = None
while True:
    print('Somente entre as opções abaixo!\n' if menu is not None else 'Escolha uma opção:\n')
    menu = input('1) Carregar lista de Tarefas\n2) Criar Lista de Tarefas\n\nDigite Aqui: ')
    
    if menu.isdecimal():
        if int(menu) > 3 or int(menu) < 1:
            continue
        elif int(menu) == 1:
            listaName = input('Digite o Nome do Arquivo: ')
            listaTarefa = importTarefas(listaName)
            break 
        
        listaTarefa = novasTarefas()
        break    
    clear()

opcoes = None
while True:
    print('Somente entre as opções abaixo!\n' if opcoes is not None else 'Escolha uma opção:\n')
    opcoes = input("1) Salvar Lista de Tarefas\n2) Apagar Item das Tarefas\n3) Restaurar ultima tarefa apagada\n\nDigite Aqui: ")
    
    if opcoes.isdecimal():
        if int(opcoes) > 4 or int(opcoes) < 1:
            continue
        
        elif int(opcoes) == 1:
            clear()
            listaName = input('Digite o Nome do Arquivo: ')
            exportTarefas(listaTarefa, listaName)
            continue
        
        elif int(opcoes) == 2:
            clear()
            numTarefa = input("Digite o numero da tarefa: ")
            backupListaTarefas = deepcopy(listaTarefa)
            popTarefas(numTarefa)
            continue
        
        elif int(opcoes) == 3:
            if backupListaTarefas is None:
                print('Nenhumk item foi apagado!')
                continue
            listaTarefa = deepcopy(backupListaTarefas)
            backupListaTarefas = None
            continue

        break    
    clear()