'''Faça um program que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''
while True:
    print('-=' * 30)
    n = int(input('Quer ver a tabuda de qual valor? '))
    if n <0:
        break
    print('-=' * 30)
    for c in range(1, 11):
        tb = n * c
        print(f'A tabuada de {n} X {c} = {tb}')
print('-=' * 30)
print('PROGRAMA DE  TABUADA ENCERRADA!')

