#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
frase=str(input('Digite o nome da cidade: ')).strip().lower()

v='santo' in frase
print('Existe Santo no nome da cidade? {}!'.format(v))