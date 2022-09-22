n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
if n1 == n2:
    print('Nessa comparação não tem maior, os dois tem mesmo valor!')
elif n1 > n2:
    print('O premeiro valor que é o {} é maior que o segundo que voce colocou que era o {}'.format(n1,n2))
else:
    print('O segundo numero que voce coloco, que era o {} é maior que {}, que foi o segundo valor que voce colocou.'.format(n2,n1))
    