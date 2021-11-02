'''for c in range (1, 10):
    print(c)
print('Fim')'''

'''
c = 1
while c < 10:
    print(c)
    c +=1 # ou 
    c = c+ 1
print('Fim')'''
'''
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')'''

'''
n = 1
while n != 0 :
    n = int(input('Digite um valor: '))
print('FIM')'''
'''
resposta == 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N]' )).upper()
print('FIM')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} números ímpares!'.format(par, impar))