"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista=[0]
m=0
for c in range(0,7):
    n=int(input('Digite um valor: '))
    for m in range(0,len(lista)):
        if n > lista[m]:
            pos=len(lista)
        else:
            pos = lista.index(lista[m])
            break
    m=m+1
    lista.insert(pos,n)
lista.remove(0)
print(lista)