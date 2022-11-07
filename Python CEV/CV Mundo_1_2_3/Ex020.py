#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random as r
n1=str(input('Aluno 1:'))
n2=str(input('Aluno 2:'))
n3=str(input('Aluno 3:'))
n4=str(input('Aluno 4:'))
n=[n1,n2,n3,n4]
s=r.sample(n,4)
print('A ordem de apresentação será {}!'.format(s))