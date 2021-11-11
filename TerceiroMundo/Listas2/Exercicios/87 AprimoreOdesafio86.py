'''Aprimore o desafio anterior 86 mostrando no final:
A) A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna
c)O maior valor da segunda coluna
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
scol = 0
maiorc = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:  # Soma de todos os pares digitados
            soma += matriz[l][c]
    print()
print(f'A soma dos pares são: {soma}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
