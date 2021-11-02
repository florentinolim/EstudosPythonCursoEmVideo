'''
Crie um programa que leia varios números inteiros pelo teclado.O programa so vai parar quando o
usuário digitar 999 ,que é a condição de parada. No final mostrar quantos números
foram digitados e qual foi a soma entre eles(descartando a flag)
'''

numero = cont = soma = 0
numero = int(input('Digite um número [999 para sair]: '))
while numero != 999:
        soma += numero
        cont = cont + 1
        numero = int(input('Digite um numero [999 para sair]: '))
print('Voce digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

