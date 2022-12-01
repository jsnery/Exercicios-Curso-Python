from os import system, path
from sys import exit
from time import sleep
import json

DIR = path.dirname(__file__)

def clear():
    system('cls')
    
def remover():
    if tarefas == []:
        print("Nada a remover!\n")
        return
    
    apagados.append(tarefas[-1])
    tarefas.pop()
    print(f'Ultimo item removido!')
    sleep(2)
    clear()
    return
    
def refazer():
    if apagados == []:
        print("Nada a restaurar!\n")
        return
    
    tarefas.append(apagados[-1])
    apagados.pop()
    print(f'Ultimo item restaurado!')
    sleep(2)
    clear()
    return

def listar():
    print('Listar:\n')
    print(*tarefas, sep='\n')
    print()

def sair():
    return exit()

def exportar():
    LISTANOME = path.join(DIR, 'tarefas.txt')
    JSONNOME = path.join(DIR, 'tarefas.json')

    with open(JSONNOME, 'w') as file:
        json.dump(tarefas, file, indent=2)

    with open(LISTANOME, 'w') as file:
        file.write('Lista de Tarefas\n\n')
        for i, tarefa in enumerate(tarefas, 1):
            file.write(f'{i}ª - {tarefa}\n') 


apagados = []
tarefas = []
opcao = None
while True:
    print('Comandos: Listar, Remover, Refazer, Exportar ou Sair\n')
    opcao = input('Digite uma tarefa ou comando: ').lower()
    comandos = {
        'listar': lambda: listar(),
        'remover': lambda: remover(),
        'refazer': lambda: refazer(),
        'sair': lambda: sair(),
        'exportar': lambda: exportar()
    }
    
    clear()
    comandos.get(opcao)() if comandos.get(opcao) is not None else tarefas.append(opcao.title())
    