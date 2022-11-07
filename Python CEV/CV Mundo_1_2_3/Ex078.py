"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista=[]

for valor in range(0,5):
    lista.append(int(input('Digite um valor:')))
for pos,valores in enumerate(lista):
    if valores==max(lista):
        print('O maior valor foi {}'.format(max(lista)),end='')
        print('O maior valor foi {} na posicao {}'.format(max(lista), pos))
    if valores == min(lista):
        print('O menor valor foi {} na posicao {}'.format(min(lista), pos))
