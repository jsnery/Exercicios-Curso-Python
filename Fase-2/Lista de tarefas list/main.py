from os import system
from sys import exit
from time import sleep

def clear():
    system('clear')
    
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

apagados = []
tarefas = []
opcao = None
while True:
    print('Comandos: Listar, Remover, Refazer ou Sair\n')
    opcao = input('Digite uma tarefa ou comando: ').lower()
    comandos = {
        'listar': lambda: listar(),
        'remover': lambda: remover(),
        'refazer': lambda: refazer(),
        'sair': lambda: sair()
    }
    
    clear()
    comandos.get(opcao)() if comandos.get(opcao) is not None else tarefas.append(opcao.title())
    
