"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def grande(*num):
    max = 0
    for valor in num:
        if valor > max:
            max=valor
    print(max)

grande(2,3,4,1,3,4,6,7,1,2,13,5,53,2)