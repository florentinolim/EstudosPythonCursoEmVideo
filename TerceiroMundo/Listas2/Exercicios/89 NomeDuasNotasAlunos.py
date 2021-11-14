'''Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
.No final mostre um boletim contendo a média de cada um e permita que o usuário possa mstrar as notas de cada aluno
individulamente'''
alunos = list()
while True:
    aluno =str(input('Informe o aluno: '))
    nota1 = float(input('Informe Nota1: '))
    nota2 = float(input('Informe Nota 2: '))
    media = (nota1 + nota2 ) / 2
    alunos.append( [aluno, [nota1, nota2] , media])
    resp = str(input('Deseja continuar S/N'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')  #Alinhamento do Menu
print('-=' * 26)
for i, a in enumerate(alunos):
      print(f'{i:<4}{a[0]:10}{a[2]:>8.1f}')
while True:
        print('-' *  35)
        opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if opc == 999:
            print('FINALIZANDO ...')
            break
        if opc <=  len(alunos)  -1 :
           print(f'Notas de {alunos[opc] [0]} são {alunos[opc] [1]}')
print('<<<   VOLTE SEMPRE    >>>')
''' se a opção  for menor que a quantidade de alunos menos 1'''
print()
print(alunos)





