"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
o final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
n=0
total=0
c=0
while n!=999:
    n=int(input('Digite um valor: '))
    total=total+n
    c+=1
print('Você digitou {} valores, o total foi de {}.'.format(c,total))