# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo !')).strip()
dividido = nome.split()
print('Seu nome completo em maiúsculo é {}!'.format(nome.upper()))
print('Seu nome completo em letras minusculas é {}'.format(nome.lower()))
print('A quantidade de letras sem espaços é {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('O primeiro nome é {} a quantidade de letras é {}'.format(dividido[0], len(dividido[0])))
