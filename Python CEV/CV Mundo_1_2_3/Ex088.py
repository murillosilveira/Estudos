"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

import random as r

n=int(input('Digite a quantidade de jogos: '))
temp=list()
lista=list()

for c in range(0,n):
    for i in range(0,6):
        x=r.randint(1,60)
        temp.append(x)
        lista.append(temp[:])
        temp.clear()
        lista.sort()
    print(f'Jogo {c+1} -> {lista}')
    lista.clear()








