n = int(input('Digite um numero: '))
if n > 0:
    f = 1
    for item in range(1,n+1):
        f = f * item
    print(f)
else:
    print('Numero invalido')