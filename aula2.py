a = 10
print(type(a))
b = 10.0
print(type(b))
aprovado = True
print(type(aprovado))
aprovado = False
print(type(aprovado))

c = 10
d = 28
print(c == d)#False
print(c > d)#False
print(c < d)#True
print(c != d)#True
print(c >= d)#False
print(c <= d)#True

#Operadores Relacionais

# not
# and
# or

print(True and True)#True
print(True and False)#False
print(False and True)#False
print(False and False)#False

print(True or True)#True
print(True or False)#True
print(False or True)#True
print(False or False)#false

print(not True)# False
print(not False)# True

#Variaveis Strings
tipo_de_pao = 'assado'
string = f'Joao e Maria comem pao {tipo_de_pao}'
print(string)
print(len(string))
string_vazia = ''
print(len(string_vazia))

a = 'abcde'
print(a[0])