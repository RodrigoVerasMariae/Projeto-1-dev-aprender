from random import randrange
n = int(input('Digite um numero: '))
a = randrange(11)
if n == a:
    print('A miserave, acertou em!!!')
elif n > a:
    print('Chutou a cima do valor gerado!!')
elif n < a:
    print('Chutou abaixo do valor!!')
    
