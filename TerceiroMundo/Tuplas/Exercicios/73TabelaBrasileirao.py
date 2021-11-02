'''Crie uma tupla com os 20 primeiros colocados da tabela do campeonato Brasileirão
de futebol, na ordem de colocação.Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela esta o time do chapecoense.
'''
tabela = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza EC',
            'Bragantino','Internacional','Corinthians','Fluminense',
            'Cuiabá','Athletico-PR','Atlético','Goianiense','São Paulo',
            'América-MG','Ceará','Santos','Bahia','Juventude','Sport','Grêmio',
            'Chapecoense')
print('←→' * 40)
print(f'A tabela do Brasileirão é: tabela {tabela}')
print('←→' * 40)

print('-=' * 40)
print(f'Letra (A) → Os cinco primeiros colocados são: {(tabela[0:5])}')
print('-=' * 40)
print(f'Letra (B) → Os ultimos 4 colocados são:{(tabela[-4:])}')
print('-=' * 40)
print(f'Letra (C) → A lista ordenada {(sorted(tabela))}')
print('-=' * 40)
print(f'Letra (D) → O chapecoense esta na posição de numero {tabela.index("Chapecoense")+1}') #Neste caso uasmos Aspas duplas ou então use o format
print('-=' * 40)
