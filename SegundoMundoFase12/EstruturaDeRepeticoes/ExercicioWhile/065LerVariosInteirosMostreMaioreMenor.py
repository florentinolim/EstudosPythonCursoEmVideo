'''
Crie um progrma que leia varios numeros inteiros pelo teclado.No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

numero = 0
cont = 0
soma = 0
maior = 0
menor = 0
while numero != 999:
   numero = int(input('Digite um numero: '))
   if numero != 999:
       soma += numero
       cont = cont + 1
   if cont == 1:
       maior = numero
       menor = numero
   else:
      if numero > maior:
         maior = numero
      if numero < menor:
         menor = numero

media = soma / cont
print(cont)
print('A media de tdos os numeros são {}'.format(media))
print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))