def soma(x, y):
    return x + y

def produto(x, y):
    return x * y

def executa(f, x):
    def ff(*args):
        return f(x, args[0])

    return ff


soma_mais_5 = executa(soma, 5)
multiplica_por_10 = executa(produto, 10)

print(soma_mais_5(10))
print(multiplica_por_10(5))