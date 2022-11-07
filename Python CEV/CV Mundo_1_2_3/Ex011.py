#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
a=int(input('Digite a altura: '))
l=int(input('Digite a largura: '))
print('A parede tem uma área de {}m², serão necessarias {:.0f} latas de tintas'.format(l*a,(l*a)/2))