#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n=float(input('Digite a quantidade de dinheiro: '))
print('Você tem {:.0f} reais, equivalentes a {:.2f} dolares!'.format(n,n/5.19))