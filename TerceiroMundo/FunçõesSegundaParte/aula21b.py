'''Escopo de variaveis'''
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela (parametros opcionais)
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
   Função criada por Gustavo Guanabara do canal curso em video
    """
    s = a + b + c
    return s

r1 = somar(3, 10, 5)
r2 = somar(4, 5)
r3 = somar(a=6, c=10)

print (f'Os resultados foram {r1}, {r2}, {r3}')
