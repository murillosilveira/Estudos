#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s='g'
while s not in 'MmFf':
    s=str(input('Por favor, digite o sexo [f] ou [m]'))
print('obrigado!')
