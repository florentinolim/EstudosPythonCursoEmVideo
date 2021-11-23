'''Dicionários'''
pessoas = {'nome': 'Reginaldo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f' Mostre o nome da pessoas: {pessoas["nome"]}')
print('-=' * 50)
print(f' Mostre  a idade da pessoa: {pessoas["idade"]}')
print('-=' * 50)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-=' * 50)
print(f'Imprimindo apenas as chaves: {pessoas.keys()}')
print('-=' * 50)
print(f'Imprimindo apenas os valores: {pessoas.values()}')
print('-=' * 50)
print(f'Imprimindo apenas os itens uma lista composta de 3 tuplas: {pessoas.items()}')
print('-=' * 50)
print('''Para cada uma das pessoas mostre a sua respecitva chave ''')
for k in pessoas.keys():
    print(k)
print('-=' * 50)
print('''Para cada uma das pessoas mostre os valores ''')
for v in pessoas.values():
    print(v)

print('-=' * 50)
print('''Para mostrar os itens precisamos usar duas chaves, k e o v da seguinte forma: ''')
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-=' * 50)
print('''Alterando de Reginaldo para Renato: ''')
pessoas['nome'] = 'Renato'
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-=' * 50)
print('''Adicionando um elemento: ''')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-=' * 50)
print('''Para apagar um item  precisamos usar o del : ''')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
