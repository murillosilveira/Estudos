#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n=int(input('Digite um numero: '))
s=0
for c in range(2,n):
    if n%c==0:
        s+=1
if s==0:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')