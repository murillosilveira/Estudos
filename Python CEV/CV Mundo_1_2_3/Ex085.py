"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
 lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
 em ordem crescente."""

import random as r

temp=[]
lista=[[],[]]


qtd=int(input('Digite a quantidade de pessoas:'))

for c in range(0,qtd):
    x=r.randint(0,100)
    if x%2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

print(lista)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares foram: {lista[0]}')
print(f' e os numeros impares foram: {lista[1]}',end='')

