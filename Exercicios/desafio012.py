#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Entre com o valor do produto !' ))
new = preco * 0.05 + preco
print('O novo preço do produto é {}'.format(new))