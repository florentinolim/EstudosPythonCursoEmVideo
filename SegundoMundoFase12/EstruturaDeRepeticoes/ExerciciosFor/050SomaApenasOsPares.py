#Desenvolva um programa que leia 6 numeros inteiros  e mostre a soma
# apenas daqueles que forem pares.Se o valor digitado for impar, ele desconsidera.
s = 0
for n in range(0, 6):
    num = int(input('Digite o {} numero:'.format(n)))
    if num % 2 == 0:
        s += num
        print('O numero digitado é par {}'.format(num))
    if num % 2 == 1:
        print('O numero digitado é impar {}'.format(num))

print(s)

