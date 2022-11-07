#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome=str(input('Digite seu nome completo: ')).split()
qtd=len(nome)
print('O primerio nome é {}!\nO ultimo nome é {}!'.format(nome[0],nome[len(nome)-1]))
