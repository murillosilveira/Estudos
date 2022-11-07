#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=10000000

for c in range(1,6):
    n=int(input('Digite o peso da pessoa {}:'.format(c)))
    if n > maior:
        maior=n
    if n < menor:
        menor=n
print('O maior peso foi {} e o menor foi {}'.format(maior,menor))