#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import random as r

aleat=r.randint(0,9999)
st=str(aleat)

print('o número digitado foi {}!\nMilhar {}!\nCentena {}!\nDezena {}!\nUnidade {}!'.format(st,st[0],st[1],st[2],st[3]))



