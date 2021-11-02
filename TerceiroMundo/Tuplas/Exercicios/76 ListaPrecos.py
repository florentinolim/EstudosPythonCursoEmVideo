''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
produtos = ('Laranja',7.00,
            'Maça',8.00,
            'Uva',12.00,
            'Alfaçe',2.00,
            'Cebola',8.00,
            'Tomate',15.00,
            'Repolho',10.00)
print(f'Os produtos da lista são:{produtos}')
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)