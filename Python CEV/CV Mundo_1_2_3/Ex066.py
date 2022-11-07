"""Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag)."""

n=0
total=0
c=0
while n!=999:
    n=int(input('Digite um valor: '))
    total=total+n
    c+=1
print('Você digitou {} valores, o total foi de {}.'.format(c,total))