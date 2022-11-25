from copy import deepcopy
from dados import Produtos, Ordenar

novos_produtos = deepcopy(Produtos)

for i in novos_produtos:
    i['preco'] = round(i['preco'] * 1.1, 2)
    
produtos_ordenados_por_nome = deepcopy(Ordenar(novos_produtos, 'nome'))
produtos_ordenados_por_preco = deepcopy(Ordenar(novos_produtos, 'preco'))

print(*produtos_ordenados_por_nome, sep='\n', end='\n\n')
print(*produtos_ordenados_por_preco, sep='\n', end='\n\n')