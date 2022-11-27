from copy import deepcopy
from itertools import zip_longest

lista1 = [5, 3, 7, 8, 4, 4, 9]
lista2 = [6, 7, 8, 9, 4, 6]


def FactorFunc(func):

    def inerFunc(*args, **kwargs):
        lista = deepcopy(args)
        x = len(lista[0])
        y = len(lista[1])
        diference = None
        if x > y:
            diference = x - y
            for i in range(diference):
                lista[1].append(0)
            return func(*lista, **kwargs)
        elif x < y:
            diference = y - x
            for i in range(diference):
                lista[0].append(0)
            return func(*lista, **kwargs)

        return func(*lista, **kwargs)

    return inerFunc

@FactorFunc
def zipper(l1, l2):
    z = max(len(l1), len(l2))
    n = [(l1[i] + l2[i]) for i in range(z)]
    return n

print([x + y for x, y in zip(lista1, lista2)])

print([x + y for x, y in zip_longest(lista1, lista2, fillvalue=0)])

print(zipper(lista1, lista2))

