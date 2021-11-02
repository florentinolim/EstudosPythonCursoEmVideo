# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
# aparece a letra "A", em que posição ela aparece a primeira
# vez e em que posição ela aparece a última vez
frase = str(input('Informe uma frase: ')).strip().upper()
print('O numero de vezes que a letra aparece no texto é {}'.format(frase.count('A')))
print('A primeira ocorrência da letra A é {}'.format(frase.find('A')+1)) # Como a contagem começa com zero a gente soma +1 pra ficar legivel
print('A Ultima ocorrência da letra A é {}'.format(frase.rfind('A')+1)) # Como a contagem começa com zero a gente soma +1 pra ficar legivel




