num = int(input('Digita um numero: '))
print('''Escolha um numero:
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal
''')
Opcao = int(input('Digita sua opção: '))
if Opcao == 1:
    print('O valor {} convertido para Binario é: {}'.format(num,bin(num)[2:]))
if Opcao == 2:
    print('O valor {} convertido para Octal é: {}'.format(num,oct(num)[2:]))
if Opcao == 3:
    print('O valor {} convertido para Hexadecimal é: {}'.format(num,hex(num)[2:]))
else:
    print('Valor invalido!')
