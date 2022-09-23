print('='*10, 'LOJA VERAS', '='*10)
preco = float(input('Qual foi o preço da compra:R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    valor = (preco*10/100)
    print('Sua compra será a vista de {:.2f}, com o desconto fica por {:.2f}.'.format(preco, (preco-valor)))
elif opcao == 2:
    valor = (preco*5/100)
    print('Sua compra será a vista de {:.2f}, com o desconto fica por {:.2f}.'.format(preco, (preco-valor)))
elif opcao == 3:
    print('Sua compra fica de duas vezes de {:.2f}'.format(preco/2))
elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    valor = (preco*20/100)
    valorfinal = valor + preco
    print('Sua compra de {:.2f}, teve aumento de 20% ficando {:.2f}, divido em {} de {:.2f}'.format(preco, valorfinal, parcela, (valorfinal/parcela)))
