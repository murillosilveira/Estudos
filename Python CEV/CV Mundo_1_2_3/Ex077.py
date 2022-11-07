"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

lista=('murillo','mercado','tati','auro')

for c in range(0,len(lista)):
    print('As vogais da palavra {} são: '.format(lista[c]),end='')
    str=lista[c]
    for d in range(0,len(str)):
        if str[d] in 'aeiouAEIOU':
            print(str[d],end='')
    print('')
