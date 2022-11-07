"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial."""

def fatorial(x,c=0):
    if c==1:
        s=x
        p=0
        for c in range(0,x-1):
            p=s*(x-1)
            print(f'{s}x{(x-1)}={p}')
            s=p
            x=x-1
    elif c==0:
        s=x
        p=0
        for c in range(0,x-1):
            p=s*(x-1)
            s=p
            x=x-1
        print(p)




fatorial(5,0)

