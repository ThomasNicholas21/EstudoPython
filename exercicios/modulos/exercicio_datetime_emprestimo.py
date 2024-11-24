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

    emprestimo = 1000000

    data_emprestimo = datetime(2020, 12, 20)
    data_pagamento_total = relativedelta(months=60) # 12 * 5 anos
    data_emprestimo_final = data_emprestimo + data_pagamento_total
    
    data_parcelas = []
    while data_emprestimo < data_emprestimo_final:
        data_parcelas.append(data_emprestimo)
        data_emprestimo += relativedelta(months=+1)


    numero_parcelas = len(data_parcelas)
    valor_parcela = emprestimo / numero_parcelas
    total_pago = valor_parcela * numero_parcelas

    for data in data_parcelas:
        print('Data:', data.strftime('%d/%m/%Y'), f'Valor: {valor_parcela:,.2f}')
    else:
        print(f'Total de parcelas pagas é {numero_parcelas} e valor total pago foi de R${total_pago:.2f}')

if __name__ == "__main__":
    main()