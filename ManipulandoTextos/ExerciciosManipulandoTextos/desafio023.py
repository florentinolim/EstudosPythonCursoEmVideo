#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe um numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A unidade deste numero é {}'.format(unidade))
print('A dezena deste numero é {}'.format(dezena))
print('A centena deste numero é {}'.format(centena))
print('A milhar deste numero é {}'.format(milhar))