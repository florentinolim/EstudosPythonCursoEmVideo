n1 = int(input('Digite um numero! '))
n2 = int(input('Digite outro numero! '))
print('A soma é {}'.format(n1+n2))

print('Poderia ser feito da seguinte forma s = n1 + n2:')
s = n1 + n2
print('A soma de dois numeros é {}'.format(s))

print('Adicionando todos os operadores na sequencia de uma só vez')
soma = n1 + n2
multiplicacao  = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponenciacao = n1 ** n2

print('A soma vale {}, \n A multiplicação vale {}, \n A divisão vale {:.3f}, A divisão inteira vale {}, A exponenciação vale {}'.format(soma, multiplicacao, divisao, divisaoInteira, exponenciacao))

print('A soma vale {}, \n A multiplicação vale {}, \n A divisão vale {:.3f}'.format(soma, multiplicacao, divisao,), end= ' ')
# o end no final pula a linha
print('A divisão inteira vale {}, A exponenciação vale {}'.format(divisaoInteira, exponenciacao))