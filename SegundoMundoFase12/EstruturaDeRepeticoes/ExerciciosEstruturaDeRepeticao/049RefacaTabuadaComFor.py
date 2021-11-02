#Refaça o desafio009, mostrando a tabuada de um numero que o usuário escolher,
# so que agora usando um laço for.
num = int(input('Digite um numero: '))
for n in range(0, 11):
    tb = num * n
    print(' A tabuda de {} X {} = {}'.format(num, n, tb))
