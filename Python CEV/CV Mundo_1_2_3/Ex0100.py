"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""

import random as r

temp = list()
lista2=list()

def somapar(*num):
    soma=0
    for valor in num:
        if valor %2==0:
            soma=soma+valor
    print(soma)


def sorteia(n):

    lista=list()
    for c in range (0,n):
        lista.append(r.randint(1,10))
    print(lista)


print(f'Os números sorteados foram:',end='')
temp=sorteia(5)
temp

