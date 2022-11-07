"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
 a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

import time

def contador(inicio,fim,passo):

    while inicio<fim+1:
        print(inicio,end= '-')
        time.sleep(1)
        inicio=inicio+passo

x=int(input('Digite o inicio: '))
y=int(input('Digite o fim: '))
z=int(input('Digite o passo: '))

print(contador(x,y,z))