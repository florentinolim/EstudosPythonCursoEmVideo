'''Trabalhando com Tuplas , Elas são imutavies '''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
'''print(len(lanche))
print(f'Exibindo todo o lanche {(lanche)}')
print('Na posição 0 ==> {}'.format(lanche[0]))
print('Na posição 1 ==>  {}'.format(lanche[1]))
print('Na posição 2 ==>  {}'.format(lanche[2]))
print('Na posição 3 ==>  {}'.format(lanche[3]))

print(f'Exibindo a posição 1 e a posição 2 descosinderando o elemento 3 ==> {(lanche[1:3])}')
print(f'Exibindo da posição 2 até o final {(lanche[2:])}')
print(f'Exibindo do inicio até o elemento 1 desconsidera o elemento 2 ==> {(lanche[:2])}')

print(f'Contando de traz para frente mostrando o elemento 2 ==>  {(lanche[-2])}')
print(f'Começando na pizza e indo até o final{(lanche[-2:])}')
print(f'Começando no suco e indo até o final{(lanche[-3:])}')'''

'''for comida in lanche:
    print(f'Eu vou comer {comida} ')
print(' Comi pra caramba')'''

'''for cont in range(0, len(lanche)):
    print(f'Eu vou comer {(lanche[cont])} na posição {cont}')
print(' Comi pra caramba e novo ')'''

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(' Comi pra caramba e novo ')'''

'''print(sorted(lanche))
print('Exibindo de forma organizada os dados com sorted {}'.format(sorted(lanche)))'''

#Concatenando uma tupla
a = 2, 5, 4
b = 5, 8, 1, 2
c = a+b
print(c)
print('O tamanho da tupla {}'.format(len(c)))
print('Contando quantas vezes o 5 aparece em c = {}'.format(c.count(5)))
print('Mostrando a posição de um numero dentro da tupla {}'.format(c.index(5)))
print('Mostrando a posição do numero 5 a partir da posição: (1) {}'.format(c.index(5, 2)))

'''Apagando uma tupla
pessoa = ('Reginaldo', '48', 'M', '90')
del(pessoa)
print('Apagando a tupla'.format(pessoa))'''