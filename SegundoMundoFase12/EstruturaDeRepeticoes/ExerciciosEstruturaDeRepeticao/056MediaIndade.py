#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo.
#aulaQual e o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
maiorIdade = 0
menorIdade = 0
contidade = 0
for n in range(1, 4):
    nome = str(input('Digite o nome da {}º pessoa: '.format(n)))
    idade = int(input('Digite a idade da {}º pessoa: '.format(n)))
    sexo = bool(input('Digite o sexo da {}º pessoa: '.format(n)))
    contidade = contidade + idade
    if n == 1:
        maiorIdade = idade
        menorIdade = idade
    else:
        if idade > maiorIdade:
            maiorIdade = idade
        if idade < menorIdade:
            menorIdade = idade

print('A maior idade é {} '.format(maiorIdade))
print('A menor idade é {}'.format(menorIdade))

media = contidade / 3
print('A media de idade do grupo é de {:.2f}'.format(media))
