#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00por cada KM acima do limite
vel = float(input('Informe a velocidade do veículo KM: '))
if vel > 80:
     print('MULTADO! Você excedeu o limite permitido de 80Km/h')
     multa = (vel-80) * 7
     print('Você ultrapassou o limite de velocidade será multado em R${:.2f}'.format(multa))
print('Continue respeitando o limite de velocidade dirija com cuidado.')
