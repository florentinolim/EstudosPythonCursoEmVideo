'''Crie um programa onde o usuário possa digitar varios valores numéricos e cadastre em uma lista.
Caso o numero já exista, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados
em ordem crescente.'''
valores = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
          print('Valor duplicado! Nõ será adicionado ...')
    resp = str(input('Deseja continuar [S/N]  ')).strip().upper()
    if resp in 'Nn':
       break
print( '-=' * 30)
valores.sort()
print(f'Você inseriu os seguintes valores: {valores}')


