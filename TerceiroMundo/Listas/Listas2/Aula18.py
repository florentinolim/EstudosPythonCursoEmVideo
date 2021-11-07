teste = list()
teste.append('Reginaldo')
teste.append(48)
#print(teste)
galera = list()
#galera.append(teste)  #(Aqui estamos efetuando uma ligação para que seja feita uma copia escreva da forma abaixo)
galera.append(teste[:]) #(Aqui estamos efetuan uma copia
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)