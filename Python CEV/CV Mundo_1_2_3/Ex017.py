#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math as m
ca=float(input('Digite o Cateto Adjacente: '))
co=float(input('Digite o Cateto Oposto: '))
h=m.sqrt(pow(ca,2)+pow(co,2))
print('A hipotenusa é {:.2f}'.format(h))
