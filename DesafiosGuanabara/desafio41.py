from datetime import date
atual = date.today().year
nome = input('Digite seu nome: ')
ano = int(input('Ano que vc nasceu: '))
id = atual - ano
if id < 9:
    print('{}, sua idade é {} e categoria é mirim!'.format(nome,id))
elif id > 9 and id < 14:
    print('{}, sua idade é {} e categoria é Infantil!'.format(nome,id))
elif id > 14 and id < 20:
    print('{}, sua idade é {} e categoria é Junior!'.format(nome,id))
elif id > 20:
    print('{}, sua idade é {} e categoria é Sénior!'.format(nome,id))