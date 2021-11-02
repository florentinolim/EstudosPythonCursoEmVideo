#Desenvolva uma lógica que leia a peso e altura de uma pesoa, calcule seu IMC e mostre seu status  de acordo com a table abaixo:
# - Abaixo de 18.5: Abaixo do peso # - Entre 18.5 e 25: peso ideal # - 25 até 30: Sobrepeso # - 30 até 40: Obesidade
# - Acima de 40: Obesidade morbida

alt = float(input('Informe sua altura: (m)'))
peso = float(input('Informe seu peso: (Kg) '))
imc = peso / (alt ** 2)
print('IMC igual {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso precisa comer mais {:.1f}'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Parabéns você esta no peso ideal {:.1f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você esta com sobrepeso precisa fechar a boca e malhar um pouco {:.1f}'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está com obesidade {:.1f}'.format(imc))
else:
    print('você esta com obesidade morbida {:.1f}'.format(imc))



