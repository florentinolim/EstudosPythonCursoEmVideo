# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíves sobre ela

n = input('Digite algo:')
print('O tipo primitivo é ', type(n))
print('O que você digitou só tem espaços? ', n.isspace())
print('O que você digitou é numerico ? ', n.isnumeric())
print('O que você digitou é apenas letras ?', n.isalpha())
print('O que você digitou é alfa numérico? ', n.isalnum())
print('O que você digitou esta em letras maiusculas ? ', n.isupper())
print('O que você digitou esta em letras minusculas ? ', n.islower())
print('O que você digitou esta capitalizada?', n.istitle())
print('Transformando em letras Maiusculas! ', n.upper())
print('Transformando em letras Minusculas! ', n.lower())
