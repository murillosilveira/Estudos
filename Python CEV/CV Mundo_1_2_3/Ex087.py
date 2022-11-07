"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz=[[],[],[]]
soma=0
terceira=0

for i in range(0,3):
    for j in range(0,3):
        x=int(input('Digite um numero:'))
        matriz[i].append(x)
        if x%2==0:
            soma=soma+x
        if j==2:
            terceira=terceira+x
for m in range(0,3):
    print(matriz[m])

seg=max(matriz[1])
print(f'A soma de todos os valores pares digitados foi: {soma}')
print(f'A soma de todos os valores da 3 coluna foi: {terceira}')
print(f'O maior valor da 2 linha foi: {seg}')

