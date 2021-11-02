#Faça um programa que calcule a soma entre todos os numeros impáres que são
# Multiplos de três a que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1 #Contando os numeros impares
        #cont += 1
        #s = s + n #Pode ser feito desta forma ou
        s += n # desta forma
        #print(n, end=' ')
print('A soma de todos os {} valores impares é {:.1f}'.format(cont, s))
print('Fim')

