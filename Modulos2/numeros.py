'''import uteis
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f' O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')'''


# Ou
from uteis import fatorial, dobro, triplo
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f' O fatorial de {num} é {fat}')
print(f' O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')