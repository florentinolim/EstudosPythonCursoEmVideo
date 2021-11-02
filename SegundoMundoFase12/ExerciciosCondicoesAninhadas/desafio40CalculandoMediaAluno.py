#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida.
#- Media abaixo de 5.0: Reprovado
#- Media entre 5.0 e 6.9: Recuperação
#- Média 7.0 ou superior Aprovado!
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota '))
media = (n1 + n2) /2
if media < 5.0:
    print('REPROVADO {}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO {}'.format(media))
else:
    print('Parabéns APROVADO {}'.format(media))
