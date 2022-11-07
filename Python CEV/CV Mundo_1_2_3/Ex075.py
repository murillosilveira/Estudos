"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
n4=int(input('Digite um número: '))
lista=(n1,n2,n3,n4)

print('O número 9 apareceu {} vezes.'.format(lista.count(9)))
if 3 not in lista:
    print('Não tem numero 3.')
else:
    print('O primeiro valor 3 foi digitado na {} posição.'.format(lista.index(3)))
print('Os números pares são: ',end='')
for c in range(0,len(lista)):
    if lista[c]%2==0:
        print('{} '.format(lista[c]),end=' ')


