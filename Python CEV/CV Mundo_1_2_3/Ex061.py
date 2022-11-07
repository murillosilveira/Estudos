"""Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."
"""

razao=int(input('Digite a razao da P.A:'))
a=int(input('Digite o primeiro termo da P.A:'))
result=a
c=1

while c <11:
    print(result,end='->')
    result=result+razao
    c+=1
print('fim')
