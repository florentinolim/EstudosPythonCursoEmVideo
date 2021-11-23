'''Faça um programa que leia o nome e a média de um aluno, guardando a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela'''
aluno = dict()
aluno['nome']= str(input('Nome: '))
aluno['media']= float(input(f'media do aluno: {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media']  < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


