from math import hypot
co = float(input('O valor do cateto oposto: '))
ca = float(input('O valor de cateto adijacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))