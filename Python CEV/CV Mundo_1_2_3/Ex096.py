"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno."""

def area(altura,largura):
    print('O terreno tem uma largura {} e uma altura {}. Sua área é {}m²!'.format(largura,altura,largura*altura))

print(area(5,89))