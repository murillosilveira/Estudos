"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

n='s'
lista=[]
count=0
while n not in 'Nn':
    f=int(input('Digite um valor: '))
    n=str(input('Quer continuar? [N] para sair'))
    count+=1
    lista.append(f)
print(f'Foram digitados {count} valores.')
lista.sort(reverse=True)
print(f'A lista de valores digitados foi: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')


