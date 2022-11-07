"""Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 5) e mostrá-lo por extenso."""


nome=('zero','um','dois','tres','quatro','cinco')
n=int(input('Digite um número: '))

while n < 0 or n > 5:
    n = int(input('Digite um número válido: '))
    while n >=0 and n <6:
        print(f'O número digitado foi {nome[n]}')
        break
