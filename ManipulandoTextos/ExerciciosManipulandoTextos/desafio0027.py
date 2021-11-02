#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome: ')).strip()
lista = nome.split()
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu útimo nome é {}'.format(lista[len(lista)-1])) #Usando a função len eu sei quantas posições tem nome assim ele me mostra a lista na posição de len de lista-1
