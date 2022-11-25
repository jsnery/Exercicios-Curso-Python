from math import prod


def produto(*args):
    # return prod(args)
    x = 1
    for n in args:
        x *= n

    return x


def imparpar(x):
    if type(x) is not int:
        return 'Você não digitou um numero inteiro'
    return 'Par' if (x % 2 == 0) else 'Impar'


produtResult = produto(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(produtResult)

oddPair = imparpar(5)

print(oddPair)
