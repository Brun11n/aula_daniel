''' valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 200
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} Cédula(s) de R$ {atual}")

        if apagar == 0:
            break
        if atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0
        '''

        # ----------------------------------------------------------------------- #
# valor = float(input("Digite o valor a pagar: "))
# cedulas = 0
# atual = 200
# apagar = valor
# while True:
#     if atual <= apagar:
#         apagar -= atual
#         cedulas += 1
#     else:
#         if atual >= 1:
#           print(f"{cedulas} Cédula(s) de R$ {atual}")
#         else:
#           print(f"{cedulas} moeda(s) de R${atual: .2f}")

#         if apagar < 0.05:
#             break
        # if atual == 200:
        #     atual = 100
        # elif atual == 100:
        #     atual = 50
        # elif atual == 50:
        #     atual = 20
        # elif atual == 20:
        #     atual = 10
        # elif atual == 10:
        #     atual = 5
        # elif atual == 5:
        #     atual = 2
        # elif atual == 2:
        #     atual = 1
        # elif atual == 1:
        #     atual = 0.5
        # elif atual == 0.5:
        #     atual = 0.25
        # elif atual == 0.25:
        #     atual = 0.1
        # elif atual == 0.1:
        #     atual = 0.05
        # elif atual == 0.05:
        #     atual = 0
        
        # cedulas = 0

'''tabuada = 1
while tabuada <=10:
    numero = 1
    while numero <= 10:
      print(f"{tabuada} X {numero} = {tabuada * numero}")

      numero += 1
    print(" ")
    tabuada += 1 '''

    #listas

# lista = [1,2,3]
# print(lista)
# lista[0] = 10
# print(lista)

# notas = [6,7,5,8,9]
# soma = 0
# x = 0
# while x < 5:
#     soma += notas[x]
#     x += 1
# print(f"Média: {soma/ x: .2f}")

notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Digite a nota {x + 1}:"))
    soma += notas[x]
    x += 1
x = 0
print(" ")
while x < 5:
    print(f"Nota {x+1}: {notas[x]}")
    x += 1
print(f"Média: {soma / x: .2f}")
