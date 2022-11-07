#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c=float(input('Digite a temperatura em celsius:'))
f=((9/5)*c)+32
print('A temperatura é {:.2f}F'.format(f))
