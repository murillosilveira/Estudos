#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s=0
for c in range(3,501,3):
    if c%2==1:
        s=s+c
print(s)