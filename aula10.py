# for x in [5, 6, 7, 8, 9, 10]:
#     print(x)

# for variavel_de_controle in range(0,20):
#     print(variavel_de_controle)

# lista = ["Daniel", "João", "Tiburtino"]

# for e in lista:
#     print(e)

# x = 0
# while x < len(lista):
#     e = lista[x]
#     print(e)
#     x += 1

# lista = [7, 9, 10, 12]

# p = int(input("Digite um número a pesquisar: "))
# for e in lista:
#     if e == p:
#         print("Elemento encontrado")
#         break
#     else:
#         print("Elemento não encontrado.")

# for imprime_9 in range(1, 10):
#     print(imprime_9)

# for t in range(3 , 33, 3):
#     print(t, end=" ")
# print()

# f = list(range(100, 1000, 50))
# print(f)

# from time import sleep
# for par in range(2,51,2):
#     print(par, end=", ")
#     sleep(0.5)
# print('Números pares até 50.....')

# for i in range(0,10):
#     print(i+1)
#     print('fim')

# for i in range(10,-1, -1):
#     print(i)
# print('fim')

# numero = int(input('Digite um número: '))
# for i in range(0, numero+1):
#     print(i)
# print('fim')

# inicio = int(input('Inicio: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))

# for i in range(inicio, fim+1, passo):
#     print(i)
# print('fim')

# soma = 0
# fim = int(input('Digite quantos números deseja somar: '))
# for i in range(0,fim):
#     numero = int(input('Digite um valor: '))
#     soma += numero
# media = soma/fim
# print(f'A soma dos números foi: {soma}, e a média foi: {media: .2f}')

from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1                                                                                         )
print('Apitou Começou!!!!')