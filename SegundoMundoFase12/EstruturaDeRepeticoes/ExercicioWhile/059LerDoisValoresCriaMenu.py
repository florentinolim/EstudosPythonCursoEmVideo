'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]mutiplicar
[3]maior
[4]novos números
[5]sair do programa
seu programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep
n1 = float(input('Digite o primeiro numero. '))
n2 = float(input('Digite o segundo numero. '))
opcao = 0
while opcao != 5:
     print('''
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos números
     [5] Sair do programa
     ''')
     opcao = int(input('>>>>>>>>>>Escolha uma das opções: '))
     if opcao == 1:
          soma = n1 + n2
          print('A soma dos {} + {} = {}: '.format(n1, n2, soma))
     elif opcao == 2:
          mult = n1 * n2
          print(' A multiplicação de {} * {} = {}'.format(n1, n2, mult))
     elif opcao == 3:
          if n1 > n2:
               print('O numero {} é maior que {}'.format(n1, n2))
          else:
               print('O numero {} é maior que {}'.format(n2, n1))
     elif opcao == 4:
          print('Informe os numeros novamente:')
          n1 = float(input('Digite o primeiro numero. '))
          n2 = float(input('Digite o segundo numero. '))
     elif opcao == 5:
          print('Finalizando...')
     else:
          print('Opção invalida. Tente novamente')
     print('=-=' * 10)
     sleep(2)
print('Fim do programa! Volte sempre!')
