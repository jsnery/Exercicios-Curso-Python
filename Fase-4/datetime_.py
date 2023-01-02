from datetime import datetime
from dateutil.relativedelta import relativedelta


data_emprestimo = datetime(2020, 12, 20)
valor_emprestimo = 1_000_000
anos_parcela = 5
meses_parcela = anos_parcela * 12
valor_parcela = valor_emprestimo / meses_parcela

fim_pagamento = data_emprestimo + relativedelta(years=anos_parcela)
duracao_dias = (fim_pagamento - data_emprestimo).days

soma = 0.0
for i in range(1, meses_parcela+1):
    contador = data_emprestimo + relativedelta(months=i)
    soma += valor_parcela
    print(f'{contador.strftime("%d/%m/%Y")} -> R${valor_parcela:,.2f}')

print(f'{soma:,.2f}')

# divida = 1_000_000

# data_emprestimo = datetime(2020, 12, 20)
# tempo = relativedelta(years=5)
# fim_pagamento = data_emprestimo + tempo
# dias = (fim_pagamento - data_emprestimo).days
# valor = divida / dias

# soma = 0.0
# parcela = 0.0
# for i in range(1, dias+1):
#     contando = data_emprestimo + relativedelta(days=i)
#     parcela += valor
#     soma += valor
#     if contando.day == 20:
#         print(f'{contando.strftime("%d/%m/%Y")} -> R${parcela:.2f}')
#         parcela = 0.0

# print(f'{soma:.2f}')
