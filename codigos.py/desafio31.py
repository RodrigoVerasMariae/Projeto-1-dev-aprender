distancia = float(input('Qual a distancia de sua viagem? '))
if distancia <= 200:
    print('O valor de sua passagem é R${:.2f}'.format(distancia*0.50))
else:
    print('O valor de sua passagem é R${:.2f}'.format(distancia*0.45))