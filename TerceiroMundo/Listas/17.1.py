'''valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'O valores são {v}...',end=' ')'''
'''for c, v in enumerate(valores):
    print(f'Os valores {c} com seus respectivos indices são:{v}')
print('Cheguei ao final da lista.')'''

''' Adicionando valores através do teclado '''
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
'''

'''Criando duas lista uma recebendo a outra'''
a = [2, 3, 4, 7]
b = a
print(f'A lista a = {a}')
print(f'A lista b = {b}')

'''print('-=' * 40)
print('Se eu altero b ele também altera a')
b[2] = 8
print(f'A lista a = {a}')
print(f'A lista b = {b}')'''
print('-=' * 40)

print('Copiando uma lista')
b = a[:]
print(f'A copia de a = {b}')
