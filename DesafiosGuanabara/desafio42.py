r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3 != r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não forma um triangulo')
    
