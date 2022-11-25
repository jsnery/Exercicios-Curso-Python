listOfintegers = [
    [1,2,3,3,2,1],
    [1,2,3,2,3,1],
    [1,2,3,4,5,6],

]

def duplicados(x):
    numeroschecados = set()
    resultado = -1

    for n in x:
        if n in numeroschecados:
            resultado = n
            break
        
        numeroschecados.add(n)

    return resultado

for listas in listOfintegers:
    print(duplicados(listas))
    print()
        





