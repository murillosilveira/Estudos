#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n=float(input('Digite o salário: '))

if n>1250:
    print('O salário foi de {:.2f}R$'.format(n*1.1))
else:
    print('O salário foi de {:.2f}R$'.format(n*1.15))
