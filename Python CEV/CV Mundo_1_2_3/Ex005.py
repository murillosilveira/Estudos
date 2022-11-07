#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
N=int(input('Digite um número inteiro: '))
print('O número digitado foi: {}!\nSeu atecessor é {}!\nSeu Sucessor é {}!'.format(N,N-1,N+1))