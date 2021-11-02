#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta,
#necessária para pinta-la. Sabendo que cada litros de tinta pinta 2m quadrados
larg = float(input('Informe a largura !'))
alt = float(input('Informe a altura !'))
area = larg * alt
cons = area / 2
print('A área quadra da parede é {:.2f}, a quantida de tinta estimada é de {:.2f}'.format(area, cons))

