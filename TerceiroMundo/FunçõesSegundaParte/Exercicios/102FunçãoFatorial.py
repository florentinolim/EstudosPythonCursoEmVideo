'''Crie um programa, que tenha uma função fatorial() que receba dois parametros:
o primeiro que indica o numero a calcular  e o outro chamdo show, que será um valor logico (opcional)
indicando se mostrará ou não na tela o processo de calculo do fatorial is None:'''
#Calculando o fatorial
'''
def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

#Programa principal
print(fatorial(5))'''

def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um numero

    :param n: O numero a ser calculado.
    :param show:(opcional) Mostrar ou não a conta
    :return: O valor do farorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1 :
                print(' x ', end=' ' )
            else:
                print(f' = ', end=' ')
        f *= c
    return f

#Programa principal
n = int(input('Digite um numeto: '))
print(fatorial(n, show=True))
#print(fatorial(n))
help(fatorial)

