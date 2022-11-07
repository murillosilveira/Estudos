"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

lista=[['murillo',75],['auro',78],['tati',65]]
c=0
#for n in range(0,4):
    #pessoa=str(input('Digite o nome da pessoa:'))
    #peso=int(input('Digite o peso:'))
    #lista.append([pessoa,peso])
    #c+=1


max=0
min=100000000
print(lista)

for i in lista:
    if i[1]>max:
        max=i[1]
    if i[1]<min:
        min=i[1]

print(f'A pessoa mais pesada pesa {max} e a mais leve pesa {min}!')
