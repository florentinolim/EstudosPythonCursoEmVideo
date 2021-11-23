estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf']= str(input('Unidade Federerativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
   # print(e)
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}.')
        for v in e.values():
            print(v, end=' ')
        print()