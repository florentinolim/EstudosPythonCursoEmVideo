'''Criando uma lista'''
num = [2, 5, 9, 1]
print(f'Valor de {num}')
num[2] = 3 # Num na posição 2 será alterado para o valor 3  de [2, 5, 9, 1] para [2, 5, 3, 1]
print(f'Valor para {num}')
print(f'Adicionando o valor 7 a lista {num.append(7)}') # Adicionando o valor 7 na lista
num.sort() #Ordenando a lista
print(num)
num.sort(reverse=True)#Ordenando de forma inversa
#num.insert(2, 0)#Inserindo na posição 2 o valor (0) pega o 3 joga pra frente e adiciona o (0)
num.insert(2, 2)#Inserindo na posição 2 o valor (2) pega o 3 joga pra frente e adiciona o (2)
num.remove(2)#Remove apenas a primeira ocorrência do valor 2
#num.pop()#Remove o ultimo valor que neste caso é o valor 1
#num.pop(2)#Remove o elemento 2 da lista que neste caso é o (0) e o 1 volta para o final.
'''Tentando remover um item que não esta na lista desta forama temos que usar o if para não gerar um erro'''
if 4 in num:
    num.remove(4)
else:
    print('Não foi encontrado o valor 4 na lista')
print(num)
print(f'Essa lista possui {len(num)} elementos')
