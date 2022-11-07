#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))
s=0
for c in range(n,n+10*r,r):
    print(c,end='->')
    s+=1
print('A soma deu {}!'.format(s))