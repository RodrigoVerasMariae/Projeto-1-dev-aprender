r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if  r1 < r2 + r3 and  r2 < r3 + r1 and r3 < r1 + r2 :
    print('Da para formar um triangulo')
else:
    print('Não forma um triangulo')

