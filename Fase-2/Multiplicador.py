def potencia(valor, *args):
    valor = valor
    if args == ():
        return 'Nenhuma potência digitada'
    elif len(args) == 1:
        return valor ** int(*args)
    
    for n in args:
        valor **= n
    
    return valor

print(potencia(5, 5))
