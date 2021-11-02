nome = str(input('Qual o seu nome? '))
if nome == 'Reginaldo':
    print('Seu nome é Maravilhoso!')
elif nome.capitalize() == 'Pedro' or nome =='Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Julina':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))

