capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro', 'Sergipe']
estados = ['BA', 'SP', 'MG', 'RJ']

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
def zipper(cap, est, z=0):
    n = []
    for i in range(z):
        n.append((cap[i], est[i]))
    return n

print(zipper(capitais, estados))