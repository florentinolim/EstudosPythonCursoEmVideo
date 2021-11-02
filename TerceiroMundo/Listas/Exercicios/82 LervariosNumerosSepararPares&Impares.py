'''Crie um programa que vai ler vários números  e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares
digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''
lista = list()
listpar = list()
listimpar = list()
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    resp = str(input('Deseja continuar [S/N]')).strip().upper()
    if resp == 'N':
        if n % 2 == 0:
            listpar.insert(n)
        else:
            listimpar.insert(n)
        break
print(f'Total de numeros da lista{lista}')
print(f'Numeros pares {listpar}')
print(f'Numeros impares{listimpar}')

