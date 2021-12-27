def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela (parametros opcionais)
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
   Função criada por Gustavo Guanabara do canal curso em video
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 10, 5)
somar(4, 5)
somar(a=6, c=10)
somar(c=10, b=35)
somar()'

'''def multiplos(* valores):
    """
    :param valores: Qualquer  quantidade de valores adicionados será somado

    """
    f = 0
    for n in valores:
        f += n
    print(f'A soma dos numeros  {valores} temos {f } ')

multiplos(100, 200, 300, 500, 1000, 2000)'''