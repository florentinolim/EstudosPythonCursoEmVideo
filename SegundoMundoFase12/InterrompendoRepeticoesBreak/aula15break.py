cont = 1
while cont <= 10:
    print(cont, '→ ', end='')
    cont += 1
print('Acabou')

'''
cont = 1
while True:
    print(cont, '→ ', end='')
    cont += 1
print('Acabou')'''
'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale{}'.format(s))
print(f'A Soma vale{s}')'''

'''nome = 'jose'
idade = 33
print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2 Vesão antiga'''