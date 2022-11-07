#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n=int(input('Digite um número inteiro: '))

bin=bin(n)
oct=oct(n)
hex=hex(n)

x=int(input('Você deseja converter o número {} para qual base? bin[1] oct[2] ou hex[3]:'.format(n)))
if x==1:
    print(bin)
elif x==2:
    print(oct)
else:
    print(hex)