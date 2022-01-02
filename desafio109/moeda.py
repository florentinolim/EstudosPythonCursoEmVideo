def aumetar(preco=0, taxa=0, formato= False):
    '''

    :param preco: Valor que será inoformado
    :param taxa: valor a ser calculado
    :param formato: Formatação de Moeda True formata, False não formata e Vazio não formata
    :return:
    '''
    res = preco + (preco * taxa)/100
    return res if formato is False else moeda(res)

def diminuir(preco=0, taxa=0, formato= False ):
    res = preco -(preco * taxa)/100
    return res if formato is False else moeda(res)

def dobro(preco=0, formato= False):
    res = preco * 2
    return res if formato is False else moeda(res)

def metade(preco=0, formato= False):
    res = preco /2
    return res if formato is False else moeda(res)

def moeda(preco=0,  moeda='R$'):
      return f'{moeda}{preco:>.2f}'.replace('.',  ',')

