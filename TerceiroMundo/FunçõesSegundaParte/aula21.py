def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return Sem retorno
    Funcão criada durante as aulas por Gustavo Guanabara Canal Curso em Video
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
print('FIM')


contador(100, 200, 10)

help(contador)


