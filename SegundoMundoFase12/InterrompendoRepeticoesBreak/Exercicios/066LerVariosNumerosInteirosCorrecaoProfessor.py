'''
Crie um programa que leia varios numeros inteiros pelo tecaldo.
O programa so vai parar quando o usuário digitar 999, que é a condição de parada. No final,
mostre quantos números foram digitados qual foi a soma entre eles desconsiderando a flag.
'''

soma = cont = 0
while True:
   num =int(input('Digite um valor (999 para parar): '))
   if num == 999:
        break
   cont += 1
   soma += num
print(f'A soma dos {cont}, valores foi {soma}' )
