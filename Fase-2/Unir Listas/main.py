from itertools import zip_longest

capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Sergipe']
estados = ['BA', 'SP', 'MG', 'RJ']

def FactorFunc(func):
    def inerFunc(*args, **kwargs):
        x = min(len(args[0]), len(args[1]))
        return func(*args, **kwargs, z=x)
    return inerFunc


def zipper(cap, est, z=0):
    x = min(len(cap), len(est))
    n = [(cap[i], est[i]) for i in range(x)]
    return n

print([(x, y) for x, y in zip(capitais, estados)])

print([(x, y) for x, y in zip_longest(capitais, estados, fillvalue='Deconhecida')])

print(zipper(capitais, estados))