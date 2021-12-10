'''Faca um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parametro e mostre uma mensagem com tamanho adaptável.

Ex: escreva(´Olá Mundo')
Saída:
~~~~~~~~
Olá Mundo
~~~~~~~~'''
def escreva(msg):
    tam = len(msg) + 3
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

#Progrma principal
escreva('Gustavo Guanabara')
escreva('Curso em video')
escreva('CEv')