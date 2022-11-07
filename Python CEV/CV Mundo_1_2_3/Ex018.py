#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math as m
n=m.radians(int(input('Digite o Angulo: ')))
print('O valor do seno é {:.2f}\nDo Cosseno é {:.2f}\nDa tangente é {:.2f}'.format(m.sin(n),m.cos(n),m.tan(n)))
