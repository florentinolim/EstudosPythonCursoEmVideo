'''
Crie um programa que leia varios numeros inteiros pelo tecaldo.
O programa so vai parar quando o usuário digitar 999, que é a condição de parada. No final,
mostre quantos números foram digitados qual foi a soma entre eles desconsiderando a flag.
'''
resp = 'S'
soma = quantidade = 0
while resp in 'Ss':
   numero =int(input('Digite um numero: '))
   if numero == 999:
        break
   quantidade += 1
   soma += numero
print(f'A quantidade de numeros digitados foi {quantidade}, O total foi de {soma}' )
