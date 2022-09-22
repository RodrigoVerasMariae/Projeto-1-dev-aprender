nome = input('Qual é seu nome: ')
nota = float(input('Sua nota: '))
if nota < 6.9 and nota >=5:
    print('{}, voce está de recuperação!'.format(nome))
elif nota >= 7:
    print('{}, voce passou!'.format(nome))
else:
    print('{}, voce está reprovado'.format(nome))