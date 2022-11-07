"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))

maior=max(n1,n2,n3)
menor=min(n1,n2,n3)
meio=(n1+n2+n3)-(maior+menor)

if menor+meio>=maior:
    print('É possível')

    if n1==n2 and n1==n3:
        print('Equilátero')
    elif n1!=n2 and n2!=n3:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não é possível')




