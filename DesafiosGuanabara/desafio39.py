from datetime import date
atual = date.today().year
nome = input('Digita seu nome: ')
ano = int(input('Qual o ano de seu nascimento: '))
idade = atual - ano
print('Quem nasceu em {}, tem {}.'.format(ano,idade))

if idade == 18:
    print('Esta na idade certa para se alistar, cuida')
elif idade > 18:
    print('Passou {} de seu alistamento, cuida!'.format(idade-18))
elif idade < 18:
    print('Falta {} para seu alistamento'.format(18-idade))