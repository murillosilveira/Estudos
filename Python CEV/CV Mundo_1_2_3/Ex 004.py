#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n1=input('Digite algo:')

print('O tipo primitivo é {}!'.format(type(n1)))
print('Tem apenas espaços?',n1.isspace()) #detecta se tem espaço
print('É um número?', n1.isnumeric())
print('É alfabetico? (tem apenas letras)',n1.isalpha())
print('É alfanumérico? (letras e numeros)',n1.isalnum())
print('Está em maiusculas?',n1.isupper())
print('Está em maiusculas?',n1.islower())
print('Está capitalizada? (primeira letra maiuscula)',n1.istitle())
