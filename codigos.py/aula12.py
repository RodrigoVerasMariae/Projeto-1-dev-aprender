'''nome = str(input('Qual é seu nome? '))
if nome == 'Rodrigo':
    print('Que belo nome vc tem em!')
elif nome in 'Sandra, Ranny, Ray':
    print('Que belo nome feminino vc tem!')
elif nome in 'Pedro, Mateus, Paulo':
    print('Nome de apostolo em, muito bonito!')
elif nome == 'Maria':
    print('Nome da mãe de Jesus!')
else:
    print('Nome normal!')
print('Tenha um otimo dia {}'.format(nome))'''

nome = str(input('Seu nome: '))
prova = float(input('Nota de sua prova: '))
trabalho = float(input('Nota de seu trabalho: '))
adicional = str(input('Fez a atividade? '))
nota = (trabalho + prova) / 2
if adicional == 'Sim':
    nota = nota + 1
if nota == 6:
    print('Foi por pouco em {} sua media foi {}.'.format(nome,nota))
elif nota > 6:
    print('Vc foi bem {}, passou com media {}.'.format(nome,nota))
elif nota < 6:
    print('Bora de recuperação {}, sua media foi {}.'.format(nome,nota))
    