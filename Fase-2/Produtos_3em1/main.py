from copy import deepcopy
from dados import Produtos, Ordenar

novos_produtos = [{**i, 'preco': round(i['preco'] * 1.1, 2)} for i in Produtos]

produtos_ordenados_por_nome = Ordenar(deepcopy(Produtos), 'nome', True)
produtos_ordenados_por_preco = Ordenar(deepcopy(Produtos), 'preco', False)

print('Lista Original:', *Produtos, sep='\n', end='\n\n')
print('Lista + 10%:', *novos_produtos, sep='\n', end='\n\n')
print('Lista ordenada por nome reverse:', *produtos_ordenados_por_nome, sep='\n', end='\n\n')
print('Lista ordenada por preco:', *produtos_ordenados_por_preco, sep='\n', end='\n\n')