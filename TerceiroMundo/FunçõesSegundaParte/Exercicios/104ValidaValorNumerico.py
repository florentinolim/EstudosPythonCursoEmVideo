'''Crie um programa que tenha a fução leiaint(), que vai funcionar de forma semelhante ao
input() do python, so que fazendo a validação para aceitar apenas um valor numérico.
EX:
n=leiaint('Digite um numero n')
'''
def leiaInt(msg):
    ok=False
    valor =0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m ')
        if ok:
            break
    return valor
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')


