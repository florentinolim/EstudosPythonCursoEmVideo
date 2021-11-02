#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. Veja o curso ...
nome = str(input('Informe seu nome completo: ')).strip()
print('Seu nome tem silva {}'.format('SILVA' in nome.upper()))



