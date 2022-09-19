from re import A


a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int(input('Terceiro numero: '))
menor = a
if b < a and b<c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print('O menor numero é o {}:'.format(menor))
print('O maior é o {}'.format(maior))
