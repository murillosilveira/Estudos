#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))
if n1>n2:
    if n1>n3:
        maior=n1
        if n2<n3:
            menor=n2
        else:
            menor=n3
    else:
        maior=n3
        if n1<n2:
            menor=n1
        else:
            menor=n2
else:
    if n2>n3:
        maior=n2
    else:
        maior=n3
    if n1<n3:
        menor=n1
    else:
        menor=n3
print('O maior número foi {}!'.format(maior))
print('O menor número foi {}!'.format(menor))
