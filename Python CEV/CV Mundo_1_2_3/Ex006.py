#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=float(input('Digite um número: '))
print('O dobro é {}, o triplo é {} e a raíz quadrada é {:.2f}!'.format(n*2,n*3,n**(1/2)))
