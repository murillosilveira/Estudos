#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time as t

for c in range(9,0,-1):
    print(c)
    t.sleep(1)
print('poww!!!!')