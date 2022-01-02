'''Reescreva a função leaiInt() que fizemos no desafio 104, incluído agora a possibilidade da
digitação de um número de tipo invalido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por favor digite um número real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


n1= leiaInt('Digite um inteiro ')
n2 = leiafloat('Digite um real: ')
print(f'O inteiro digitado foi:  {(n1)} e o Real digitado foi {n2}')
