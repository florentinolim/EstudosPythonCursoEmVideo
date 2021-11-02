titulo = 'Manipulando Cadeias de textos'
print('{:=^100}!'.format(titulo))

frase = 'Curso em Vídeo Python'
print(frase)
print('Fatiando a quarta letra é {:=^20} lembrando que a contagem inicia em 0 :'.format(frase[3]))
print('Fatiando da quarta letra até a letra 13: {:=^20}'.format(frase[3:13]))
print('Fatiando do inicio até a letra 13 {:=^20} '.format(frase[:13]))
print('Fatiando do inicio da letra 13 até o final: {:=^20}'.format(frase[13:]))
print('Fariando da letra 1 até a letra 15 {:=^20}'.format(frase[1:15]))
print('Fatiando da letra 1 até a letra 15 pulando de dois em dois {:=^20}'.format(frase[1:15:2]))
print('Fatiando até o final pulando de dois em dois quando não sabemos o final. colocasse o 1::2{:=^20}'.format(frase[1::2]))
print('Fatiando sem saber o inicio e o final pulando de dois em dois usa-se ::2 {:=^20}'.format(frase[::2]))

print('Contando quantas letras (o) minusculo {:=^20} tem na frase'.format(frase.count('o')))
print('Colocando a frase em maiuscula e contando quantos (O) maiusculo {:=^20} tem ana frase'.format(frase.upper().count('O')))
print('Usando a função interna len para saber quantas letras tem na frase {:=^20}'.format(len(frase)))
print('Removendo os espaços indesejados antes e depois da frase {:=^20}'.format(len(frase.strip())))
print('Usando a função replace para trocar a palavra python por android {:=^20}'.format(frase.replace('Python', 'Android')))
print('Imprima frase na posição zero {:=^20}'.format(frase[0]))
print('Buscando a palavra vídeo em minusculo, porem transformando tudo para minusculo antes {}'.format(frase.lower().find('vídeo')))
print('Crie uma lista com a frase splitando ela {}'.format(frase.split()))

dividido = frase.split()
print('Imprima apenas a primeira lista {}'.format(dividido[0]))
print('Imprima apenas na segunda lista a letra 3 :{}'.format(dividido[2][3]))

print('Curso'in frase.format(frase))
print('Buscando a palavra dentro de frase {:=^20}'.format(frase.find('Video')))


frase = 'Curso em Video Python'
print('Atribuindo a alteração para frase')
frase = frase.replace('Python', 'Android')
print('A frase agora passou a ser: {:=^20}'.format(frase))


texto = 'Imprimindo um texto grande na tela'
print('{:=^100}!'.format(texto))
print("""O SENHOR é o meu pastor, nada me faltará.
Deitar-me faz em verdes pastos, guia-me mansamente a águas tranqüilas.
Refrigera a minha alma; guia-me pelas veredas da justiça, por amor do seu nome.
Ainda que eu andasse pelo vale da sombra da morte, não temeria mal algum, porque tu estás comigo; a tua vara e o teu cajado me consolam.
Preparas uma mesa perante mim na presença dos meus inimigos, unges a minha cabeça com óleo, o meu cálice transborda.
Certamente que a bondade e a misericórdia me seguirão todos os dias da minha vida; e habitarei na casa do Senhor por longos dias.
Salmos 23:1-6""")
print('='*100)


