lista1 = [5, 3, 7, 8, 4]
lista2 = [6, 7, 8, 9, 4, 6]

def FactorFunc(func):
    def inerFunc(*args, **kwargs):
        x = len(args[0])
        y = len(args[1])
        if x > y:
            return func(*args, **kwargs, z=y)
        elif x < y:
            return func(*args, **kwargs, z=x)
        return func(*args, **kwargs, z=x)
    return inerFunc

@FactorFunc
def zipper(l1, l2, z=0):
    n = []
    for i in range(z):
        n.append(l1[i] + l2[i])
    return n

print(zipper(lista1, lista2))