lista1 = [5, 3, 7, 8, 4, 4, 9]
lista2 = [6, 7, 8, 9, 4, 6]

def FactorFunc(func):

    def inerFunc(*args, **kwargs):
        x = len(args[0])
        y = len(args[1])
        repeatNumber = None
        diference = None
        if x > y:
            diference = x - y
            for i in range(diference):
                args[1].append(0)

            repeatNumber = len(args[0])
            return func(*args, **kwargs, z=repeatNumber)
        elif x < y:
            diference = y - x
            for i in range(diference):
                args[0].append(0)

            repeatNumber = len(args[1])
            return func(*args, **kwargs, z=repeatNumber)

        return func(*args, **kwargs, z=x)

    return inerFunc

@FactorFunc
def zipper(l1, l2, z=0):
    n = [(l1[i] + l2[i]) for i in range(z)]
    return n

print(zipper(lista1, lista2))