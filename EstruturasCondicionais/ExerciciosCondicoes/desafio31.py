#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200KM e R$0.45 para viagens mais longas.
dist = float(input('Infome a distancia a ser percorrida: KM '))
if dist <= 200:
    print('O preço da passagem será: R${}'.format(dist * 0.50))
else:
    print('O preço da passagem será: R${}'.format(dist * 0.45))


