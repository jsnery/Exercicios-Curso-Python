
def repetidos(lista):
    numerosInspec = set()

    for i in lista:
        if i in numerosInspec:
            return i
        
        numerosInspec.add(i)

    return -1

numeros = [
    [1,5,4,3,2,6,7,8,4,3,2],
    [4,3,6,5,8,6,7,8,9,4,2],
    [8,5,3,4,5,6,7,3,1,7,8],
    [5,2,6,7,8,5,3,2,7,9,3],
    [1,2,3,4,5,6,7,8,9,10]
]

for conjunto in numeros:
    print(conjunto, repetidos(conjunto))