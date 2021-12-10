def cubico(comp, larg, esp):
     a = comp * larg * esp
     print(f' O metro cubico da madeira foi de {comp} x {larg} x{esp} de {a} ')


#programa principal
c = float(input('comprimento: '))
l = float(input('largura: '))
e = float(input(('Espessura')))

cubico(c, l, e)
