"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas."""

import random as r

lista=[]
lista_par=[]
lista_impar=[]

termos=int(input('Digite a quantidade de termos: '))

for c in range(0,termos):
    n=r.randint(0,99)
    lista.append(n)
    if n%2==0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'lista:{lista}')
print(f'lista par:{lista_par}')
print(f'lista impar:{lista_impar}')


