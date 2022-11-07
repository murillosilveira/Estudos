#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
n=int(input('Digite a velocidade do carro: '))

if n>80:
    print('Você se fodeu e foi multado em {}R$'.format((n-80)*7))
else:
    print('Motorista conciente')