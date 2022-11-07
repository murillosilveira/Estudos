"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""

n=int(input('Digite um numero:'))
m=1
while n>=0 and m<12:
    print('{} x {} = {}'.format(n,m,n*m))

    m+=1
    if m==11:
        m=1
        n = int(input('Digite um numero:'))