#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
import random as r
soma=0
for c in range(1,7):
    n=r.randint(1,50)
    if  n%2==0:
        soma=soma+n
        print(n)
print(f'A soma deu {soma}')