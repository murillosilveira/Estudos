"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta."""

matriz=[[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        x=int(input('Digite um numero:'))
        matriz[i].append(x)
for m in range(0,3):
    print(matriz[m])