''''nome = str(input('Qual seu nome?')).strip()
print('No seu nome pussui Veras? {}'.format('veras' in nome.lower()))'''

# Exemplo utilizando media
n1 = int(input('Nota da prova: '))
n2 = int(input('Nota do trabalho? '))
media = (n1+n1)/2
print('Sua media foi {}'.format(media))
if media >= 5:
    print('Ufa, passou em')
else:
    print('Tenha vergonha, vá estudar')
