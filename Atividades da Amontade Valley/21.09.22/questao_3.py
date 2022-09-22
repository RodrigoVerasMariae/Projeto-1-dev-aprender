n = int(input('Digita um numero: '))
n1 = int(input('Digita um numero: '))
p = str(input('Qual é a operação que vc deseja operar +, -, / ou *?'))
if p == '+':
    p = n + n1
elif p == '-':
    p = n - n1
elif p == '/':
    p = n/n1
elif p == '*':
    p = n*n1
print('O valor {p} é: {type(p)},{} e {}'.format())