'''
a = 'abcde'
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#print(a[5]) NAO EXISTE

b = "ABC" + "DE"
print(b)
c = 'D' * 8
print(c)

c = "-x-" * 9
d = "-x-" * 9
e = "-x-" * 9
print(c)
print(d)
print(e)
f = d + " 4$ = " + e * 4

#g = "Daniel"
#h = 10
#print(g + h) Isso não pode em python

anos = 10
print('João tem %d anos' % anos)

# %d --> intiros
# %s ---> Strings
# %f ----> Numeros flutuantes

#"%03d"

idade = 27
print('%d' % idade )
print('%3d' % idade )
print('%03d' % idade )

reais = 250.5000
print('R$%5.2f' % reais)
print(f'R${reais: .2f}')

i = "ABCDEFG"
print(i[::-1])
print(i[0:1])
print(i[1:2])
print(i[2:4])
print(i[0:5])
print(i[:6])

j = "DVD da XUXA ao contrário"
print(j[::-1])

divida = 0
compra = 100
divida = compra + divida
compra = 200
divida = compra + divida
compra = 300
divida = compra + divida
compra = 0
print(divida)
'''
# Entrada de Dados

x = input("Digite aqui um texto qualquer: ")
print(f'##########')
print(f'O texto digitado foi {x}')

nome = input("digite seu nome aqui: ")
print(f'Voce digitou seu nome aqui: {nome}')

numero = input("Digite um número")
print(type(numero))

reais = float(input('Digite um valor para reais: '))
print(f'Voce tem apenas R${reais: .2f}')
