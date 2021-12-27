'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situação (opcional)

Adicione também os docStrings da função
'''
def notas(*n, sit = False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varios)
    :param sit:  valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionários com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >=7:
            r['Situação'] = 'BOA'
        elif r['media']  >=5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


#programa principal

resp = notas(2.5, 5.5, 2, 2.5, 6.5,  sit=True)
#resp = notas(2.5, 5.5, 2, 2.5, 6.5)
print(resp)
#help(notas)