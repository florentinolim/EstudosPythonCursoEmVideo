#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
# normal e a condição de pagamento:
# - À vista dinheiro /cheque: 10 % de desconto
# - A vista no cartão: 5%  de desconto
# - Em até duas vezes no cartão: preço normal
# - Três vezes ou mais no cartão: 20% de juros
print('{:=^40}'.format(' ORGANIZAÇÕES GUANABARA '))

preco = float(input('Qual o preço das compras? : '))
print('''FORMAS DE PAGAMENTO: 
[ 1 ] A vista dinheiro / cheque 10%  de desconto
[ 2 ] A vista Cartão de credito 5% de desconto
[ 3 ] Em até 2X no cartão: preço normal
[ 4 ] Em até 3X ou mais no cartão: 20% de juros
''')
opcao = int(input('Qual a forma de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 /100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total /2
elif opcao == 4:
    total = preco +(preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total /totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totalparc, total))
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
else:
    total = preco
    print('Opção invalida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))




