#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))

maior=max(n1,n2,n3)
menor=min(n1,n2,n3)
meio=(n1+n2+n3)-(maior+menor)

if menor+meio>=maior:
    print('É possível')
else:
    print('Não é possível')
