#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random as r


n=int(input('Digite um valor entre 0 e 5: '))

p=r.randint(0,5)
print('O número digitado foi {} e o número sorteado foi {}!'.format(n,p))
if n==p:
    print('Parabéns, você venceu!')
else:
    print('Parabéns, você perdeu!')

