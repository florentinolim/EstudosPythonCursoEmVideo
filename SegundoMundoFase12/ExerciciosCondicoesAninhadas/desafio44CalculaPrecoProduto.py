#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e a condição de pagamento:
# - À vista dinheiro /cheque: 10 % de desconto
# - A vista no cartão: 5%  de desconto
# - Em até duas vezes no cartão: preço normal
# - Três vezes ou mais no cartão: 20% de juros
valprod = float(input('Informe o valor do produto: '))
print('''Escolha a forma de pagamento: 
[ 1 ] A vista dinheiro / cheque 10%  de desconto
[ 2 ] A vista Cartão de credito 5% de desconto
[ 3 ] Em até duas vezes no cartão: preço normal
[ 4 ] Três vezes ou mais no cartão: 20% de juros
''')
opcao = int(input('Escolha a forma de pgamento: '))
if opcao == 1:
    desconto = (valprod * 10)/100
    produto = valprod - desconto
    print('O valor do produto {:.2f} para pagamento {:.2f}:'.format(valprod, produto))
elif opcao == 2:
    desconto = (valprod * 5)/100
    produto = valprod - desconto
    print('O valor do produto {:.2f} para pagamento {:.2f}:'.format(valprod, produto))
elif opcao == 3:
    total = valprod /2
    print('O valor do produto paracelado em duas vezes é {:.2f}, parcelas de  {:.2f} '.format(valprod, total))
elif opcao == 4:
    cond = float(input('informe o numero de vezes:'))
    juros = (valprod * 20)/100
    produto = valprod + juros
    parcelas = produto /cond
    print('O valor do produto para pagamento em {} vezes é {} com parcelas de {} :'.format(cond, produto, parcelas))
else:
    print('Essa forma de pagamento não existe, escolha a forma de pagamento descrita:')





