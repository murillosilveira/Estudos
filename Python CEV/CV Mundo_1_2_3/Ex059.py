"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""


n=float(input('Digite um valor: '))
m=float(input('Digite outro valor: '))

c=int(input('[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números,[ 5 ] sair do programa)'))
while c > 0 and c < 5:

    if c==1:
        print('O resultado é {}!'.format(m+n))
    elif c==2:
        print('O resultado é {}!'.format(m * n))
    elif c==3:
        print('O resultado é {}!'.format(max(m,n)))
    elif c==4:
        n = float(input('Digite um valor: '))
        m = float(input('Digite outro valor: '))
    c=int(input('[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números,[ 5 ] sair do programa)'))