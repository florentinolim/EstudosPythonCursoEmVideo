#Codigo 1
'''def contador(*num):
    for valor in num:
        print(f'{valor} ', end=' ')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#Codigo2 Empacotando
'''def contador (* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

#Usando listas
'''def dobra(lst):
    pos = 0
    while  pos < len(lst):
        lst[pos] *= 2
        pos +=1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

#Usando desempacotamento
def soma(* valores):
       s = 0
       for num in valores:
            s += num
       print(f'Somando os valores {valores} temos{s}')


soma(5, 2)
soma(2, 9, 4)

