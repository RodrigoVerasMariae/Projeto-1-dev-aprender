from re import I


num = int(input('Digita um numero: '))
n= num % 2
if n == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMP'.format(num))