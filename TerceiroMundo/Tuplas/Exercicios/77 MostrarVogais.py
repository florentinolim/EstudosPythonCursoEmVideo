'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('maria', 'Joao', 'pedro', 'sandra', 'julia', 'alemanha', 'espanha', 'franca')
print(f'As palavras da minha lista são: {palavras}')
print('-=' * 30)
print(F'{"PALAVRAS":^40}')
print('-=' * 30)
for p in palavras:
    print(f'\nA palavra contem as seguintes vogais: {p.upper()}', end=' ')
    for letra in p:
        if letra.lower() in 'aáãaeéêiíoóuú':
            print(letra,letra.count(letra),end=' ')


