#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n=float(input('Digite um número em metros'))
print('O numero digitado tem {} centímetros e {} milimetros!'.format(n*100,n*1000))