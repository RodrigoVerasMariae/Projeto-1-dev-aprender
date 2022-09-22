nome = input('Digite seu nome: ')
valor_casa = float(input('Qual é o valor da casa: '))
salario = float (input('Qual é o seu salario: '))
anos_d_pagamento = float(input('Em quantos anos deseja pagar: '))

valor_mensal = (valor_casa / anos_d_pagamento) /12
condicao = (valor_mensal * 30/100) + valor_mensal

if salario >= condicao:
    print('Senhor {} o valor mensal fica em {:.2f}'.format(nome,valor_mensal))

elif salario < condicao:
    print('senhor {}, valor a pagar {:.2f}, exerdeu seu salario {:.2f}'.format(nome, condicao, salario))
    