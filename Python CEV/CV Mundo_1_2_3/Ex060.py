"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:"""

import math as m

n=int(input('Digite um numero:'))

print('O fatorial desse número é: {}!'.format(m.factorial(n)))
f=1
while n >= 2:
    f=f*n
    n=n-1
print('O fatorial desse número é: {}!'.format(f))