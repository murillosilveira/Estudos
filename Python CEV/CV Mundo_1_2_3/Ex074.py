"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

import random as r

lista=(r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100))

maior=max(lista)
menor=min(lista)

print(sorted(lista))
print(f'Maior = {maior}')
print(f'Menor = {menor}')