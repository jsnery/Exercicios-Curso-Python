import json
from os import path, system
from itertools import count
from salvar import Pessoa, JSONNAME

contador = count(1)

with open(JSONNAME, 'r') as file:
    dados = json.load(file)

index = {f'pessoa{next(contador)}': Pessoa(**p) for p in dados}

print(index)




