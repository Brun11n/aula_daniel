'''
dias = int(input('Quantos dias: '))
horas = int(input('Quantas horas: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos segundos: '))

dia = (60*60)*24
hora = 60*60
minuto = 60
segundos_totais = (dia * dias) + (hora * horas) + (minuto * minutos) + segundos

print(segundos_totais) '''

'''
Condicional IF
if <condição>:                  
    bloco verdadeiro
    '''

'''a = int(input('primeiro valor: '))
b = int(input('segundo valor:'))

if a > b:
    print('O primeiro valor é o maior!')
if b > a:
    print('O segundo valor é o maior!')
if a == b:
    print('Os valores são iguais!!!')


print('Fim do programa')
'''
'''
idade = int(input('Digite a idade do seu carro: '))
if idade <= 3:
    print('O seu carro é novo!!!')
if idade > 3:
    print('Seu carro é velho !!!')
'''
'''
velocidade = int(input('Digite a velocidade do seu carro: '))
multa = velocidade * 5
if velocidade > 80:
    print(f'Voce foi multado em R$ {multa}')

    if velocidade < 80:
        print('Tu deu sorte')
'''
print('Digite 3 números')
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')

