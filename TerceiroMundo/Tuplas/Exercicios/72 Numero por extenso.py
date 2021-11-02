'''Crie um programa que tenha um tupla totalmete preenchida com uma contagem por extenso de zero a vinte
seu programa deverá ler um numero pelo teclado entre zero e vinte e mostra-lo por extenso'''

cont = ('Zero','Um','Dois','três','Quatro',
        'Cinco', 'Seis','Sete','Oito','Nove',
        'Dez','Onze','Doze','Treze','Catorze',
        'Quinze','Dezesseis','Dezessete','Dezoito',
        'Dezenove','Vinte')
print(cont)

while True:
    num = int(input('Digite um número entre 0 e 20 : '))
    if 0 <= num <= 20:
        print(f'Você digitou o número: {cont[num]}')
    else:
        print('Digite o numero corretamente entre 0 e 20,')
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja Continuar S/N')).upper().strip()
    if resp == 'N':
        break



'''Exemplo do livro intensivão de python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)'''








