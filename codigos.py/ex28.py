from random import randint
from time import sleep


computador = randint(0,5) # PC vai pensar em um numero
print('=' * 11)
print('Vamos jogar')
print('=' * 11)
jogador = int(input('Em que numero estou pensado?')) # Jogador coloca um numero
print('Será que vc acertou em?')
sleep(3)
if jogador == computador:
    print('='*10)
    print('Parabens voce ganhou')
    print('=' *10)
else:
    print('='*10)
    print('Ganhei, pensei no numero {}'.format(computador))
    print('='*10)