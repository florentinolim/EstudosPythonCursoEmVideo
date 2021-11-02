#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento
sal = float(input('inrforme o salario R$'))
salNovo = (sal * 15)/100 + sal
print('O salario ficou de R${:.2f} para novo salario R${:.2f}'.format(sal, salNovo))

