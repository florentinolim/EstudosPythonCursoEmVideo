'''Aprimore o desafio anterior 86 mostrando no final:
A) A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna
c)O maior valor da segunda coluna
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if c % 2 == 0:
            
        print(f'[{matriz[l][c]:^5}]', end='')

    print()