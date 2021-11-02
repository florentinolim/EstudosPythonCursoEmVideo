for c in range(1, 6):
    print('oi')
print('FIM')
print('=+' *30)
print('Contando de trás para frente.')
for c in range(6, 0, -1):
    print(c)
print('FIM')
print('=+' *30)
print('Contando de 0 a 7 pulando de dois em dois')
for c in range(0, 7, 2):
    print(c)
print('FIM')
print('=+' *30)
n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)
print('FIM')
print('=+' *30)
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIM')
print('=+' *30)
i = int(input('Inicio: '))
f = int(input('Fim:' ))
p = int(input('Passo:')) # Pulando
for c in range(i, f+1, p):
    print(c)
print('FIM')