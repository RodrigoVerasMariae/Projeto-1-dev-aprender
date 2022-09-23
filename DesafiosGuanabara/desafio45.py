from random import randrange
itens = ('Pedra', 'Papel','Tesoura')
computador = randrange(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
print('-='*10)
jogador = int(input('Qual é a sua jogada?'))
print('-='*10)
print('-='*13)
print('O computador escolheu {}'.format(itens[computador]))
print('Voce jogou {}'.format(itens[jogador]))
print('-='*13)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Voce venceu!')
    else:
        print('Computador ganhou!')

elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('Voce perdeu!')
    elif jogador == 1:
        print('Empate!')
    else:
        print('Voce ganhou!')

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Voce ganhou!')
    elif jogador == 1:
        print('Voce perdeu!')
    else:
        print('Empate!')
print('-='*13)