"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

n=int(input('Digite os termos para sequencia de fibonacci: '))
atual=0
prim=0
seg=0
a=0
c=0
while c<=n:
    seg=prim
    prim=atual

    print(atual,end='->')
    atual=prim+seg
    if atual==0:
        atual=1
    c=c+1
print('fim')

