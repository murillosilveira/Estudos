#Exercício Python 54: Crie um programa que leia o ano de nascimento de duas pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

x=0
y=0

for c in range(0,3):
    n=int(input('Digite o ano de nascimento: '))
    if (2022-n)<18:
        x+=1
    else:
        y+=1
print('Ao todo {} maiores de idade e {} menores.'.format(y,x))