salario = float(input('Qual é o seu salario: '))
if salario > 1250:
    aumento = (salario*10)/100
    print('Seu salario vai ter aumento de {:.2f}'.format(aumento+salario))
if salario <= 1250:
    aumento = (salario*15)/100
    print('Seu aumento vai ser de {:.2f}'.format(aumento+salario))
