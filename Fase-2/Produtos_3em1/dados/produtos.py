Produtos = [
    {'nome': 'Abacaxi', 'preco': 12.56},
    {'nome': 'Bujão', 'preco': 50.35},
    {'nome': 'Grill', 'preco': 122.40},
    {'nome': 'Frango', 'preco': 16.40},
    {'nome': 'Air Fryer', 'preco': 462.40},
]

def Ordenar(x, y):
    return sorted(x, key=lambda n: n[y])