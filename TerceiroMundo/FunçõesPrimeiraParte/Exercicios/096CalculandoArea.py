'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de
um terreno retangular (largura e comprimento)e mostre a área do terreno.'''
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno{larg} x{comp} é de {a} mt2')


#Progrma principal
print('   Calculando Terreno   ')
print('-' * 35)
l = float(input('Informe a largura do terreno (m): '))
c = float(input('informe o comprimento do terreno (m): '))

area(l, c)
