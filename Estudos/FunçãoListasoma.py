valores = list()
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    resp = str(input('Deseja continuar S/N')).strip().upper()
    if resp in 'Nn':
         break
print(f'Valores inseridos {valores}')


def soma(valores):
    s = 0
    for numero in valores:
         s += numero
print(f'A soma dos valores é {valores}, {s}')


soma()