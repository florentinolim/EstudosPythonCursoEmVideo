#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Qual a temperatura ºC !'))
f = c * 1.8 + 32
f2 = 9 * c / 5 + 32
print('A temperatura de graus Celsius ºC= {} para Fahrenheit é ºF = {}'.format(c, f))
print('A segunda forma de calcular é {:.2f}'.format(f2))