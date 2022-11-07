#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
frase=str(input('Digite o nome: ')).strip().lower()

v='silva' in frase
print('Existe silva no nome? {}!'.format(v))