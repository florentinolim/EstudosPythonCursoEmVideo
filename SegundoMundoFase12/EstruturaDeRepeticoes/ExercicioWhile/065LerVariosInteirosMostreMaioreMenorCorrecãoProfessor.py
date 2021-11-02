'''
Crie um progrma que leia varios numeros inteiros pelo teclado.No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
quantidade = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    resp = str(input('Quer continuar [S/N]'.format(resp))).strip()[0]
    quantidade += 1
    soma += num

    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quantidade
print('A media dos numeros digitados é {:.2f}'.format(media))
print('O maior numero digitado é {} e o menor numero digitado é {}'.format(maior, menor))
