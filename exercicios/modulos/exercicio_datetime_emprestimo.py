# Exercício: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

def main():
    usuario = 'Maria'
    emprestimo = 1000000
    parcela = 60
    valor_mensal = emprestimo / parcela
    valor_total_pago = 0

    data_emprestimo_inicial = datetime(2020, 12, 20)
    data_pagamento_total = relativedelta(months=60) # 12 * 5 anos
    data_pagamento_mensal = relativedelta(months=1)
    data_emprestimo_final = data_emprestimo_inicial + data_pagamento_total
    
    while data_emprestimo_inicial < data_emprestimo_final:
        valor_total_pago += valor_mensal
        data_emprestimo_inicial += data_pagamento_mensal
        print(f'data: {data_emprestimo_inicial} Valor Pago: {valor_total_pago:.2f} ')
        
        if valor_mensal == emprestimo:
            print('Total pago')
    
    else:
        print(f'{usuario} pagou {valor_total_pago}')

if __name__ == "__main__":
    main()