#Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1250.00, calcule um aumentode 10%
#para os inferiores ou iguais o aumento é de 15%

sal = float(input('Informe o salário do funcionario R$ '))
if sal <= 1250.00:
    sal = (sal * 15)/100 + sal
    print('Salário é R${:.2f}'.format(sal))
else:
    sal = (sal * 10 )/100 + sal
    print('O salario é R${:.2f}'.format(sal))