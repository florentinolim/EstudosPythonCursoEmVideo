'''
Crie um programa que leia varios números inteiros pelo teclado.O programa so vai parar quando o
usuário digitar 999 ,que é a condição de parada. No final mostrar quantos números
foram digitados e qual foi a soma entre eles(descartando a flag)
'''

numero = 0
soma = 0
cont = 0
while numero != 999:
    numero = int(input('Digite um numero: '))
    if numero != 999:
        soma += numero
        cont = cont + 1
print(soma)
print(cont)

