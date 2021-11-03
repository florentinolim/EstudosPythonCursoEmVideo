'''Crie um programa onde o usúário possa digitar cinco valores númericos e cadastre-os em uma
posição da lista, já na posição correta de inserção(Sem usar o sort()).
No final mostre a lista ordenada'''
numeros = list()
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > numeros[-1]: # se o c for igual a zero ou numero maior que o ultimop
        numeros.append(n)
        print('Adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('-=' *30)
print(f'Os valores digitados em ordem foram {numeros}')
