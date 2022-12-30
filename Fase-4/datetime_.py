from datetime import datetime
from dateutil.relativedelta import relativedelta


divida = 1000000

data_emprestimo = datetime(2020, 12, 20)
tempo = relativedelta(years=5)
fim_pagamento = data_emprestimo + tempo
dias = (fim_pagamento - data_emprestimo).days
valor = divida / dias

parcela = 0.0
for i in range(1, dias+1):
    contando = data_emprestimo + relativedelta(days=i)
    parcela += valor
    if contando.day == 20:
        print(f'{contando.strftime("%d/%m/%Y")} -> R${parcela:.2f}')
        parcela = 0.0
