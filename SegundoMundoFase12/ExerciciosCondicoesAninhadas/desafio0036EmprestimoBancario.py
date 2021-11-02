#Escreva um programa para aprovar o empréstimo bancario para compra de uma casa.O programa vai perguntar
#O valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.
ValCasa = float(input('Informe o valor da casa: R$ '))
Salario = float(input('Informe o seu salário: R$ '))
Anos = int(input('Informe em quantos anos vai pagar o imovel: '))

ConvMes = Anos / (1/12)
ValApagar = ValCasa / ConvMes
PercentualSalario = Salario * 30 /100
if ValApagar > PercentualSalario:
  print('O valor da parcela de R${:.2f},\n 30% do seu salário é R${:.2f}\n {}, Anos para pagamento  NEGADO o empréstimo'.format(ValApagar, PercentualSalario, Anos))
else:
  print('Empréstimo aprovado parcela de R${:.2f},\n 30% do salario é R${:.2f}\n Salário de {:.2f}, \n {}, Anos para pagamento '.format(ValApagar, PercentualSalario, Salario , Anos))

