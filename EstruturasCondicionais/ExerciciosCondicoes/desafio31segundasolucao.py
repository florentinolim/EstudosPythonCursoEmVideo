distancia = float(input('Qula é a distância de sua viagem ?'))
preco = distancia * 0.50 if distancia<=200 else distancia * 0.45
print(' preço de sua passagem será de R${:.2f}'.format(preco))
