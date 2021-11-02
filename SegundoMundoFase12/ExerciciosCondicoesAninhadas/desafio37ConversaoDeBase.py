#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão -1 para binario  -2 para octal  -3 para hexadecimal
num = int(input('Informe um numero: '))

print('''Informe a base de conversão:
[ 1 ] converter para BINÀRIO
[ 2 ] conveter para OCTAL
[ 3 ] concerter paara HEXADECIMAL''')

opcao = int(input('Escolha opção: '))
if opcao == 1:
    print('{} valor da base de conversão é binario {}:'.format(num, bin(num)[2:]))
elif opcao == 2:
   print('{} valor da base de conversão é octal {}:'.format(num, oct(num)[2:]))
elif opcao == 3:
   print('{}  valor da base de conversão é {} :'.format(num, hex(num)[2:]))
else:
    print('Opção invalida tente novamente.')