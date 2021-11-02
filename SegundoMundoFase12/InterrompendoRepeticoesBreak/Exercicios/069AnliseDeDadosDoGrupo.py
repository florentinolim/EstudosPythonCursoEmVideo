'''Crie um programa que leia a idade e o sexo de varias pessoas.A cada pesoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
A) Quantas pessoas tem mais de 18 anos.
B: Quantos homens fora cadastrados:
C) Quantas mulheres tem menos de 20 anos:
'''
cont = 0
contSexo = 0
contF = 0
while True:
     idade = int(input('Digite a idade: '))
     if idade >18:
         cont +=1
     sexo = '  '
     while sexo not in 'MF':
         sexo = str(input('Digite o sexo [F/M]')).strip().upper()[0]
     if sexo == 'M':
         contSexo +=1
     if sexo == 'F' and idade < 20:
         contF +=1
     resp = 'S/N'
     while resp not in 'SN':
        resp = str(input('Deseja continuar[S/N]')).strip().upper()[0]
     if resp == 'N':
        break

print(f'Pessoas maiores de 18 anos: {cont}')
print(f'Pessoas do sexo masculino: {contSexo}')
print(f'Mulheres menores de 20 anos igual: {contF}')

