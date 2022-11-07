"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
eu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

lista=[]

n=str(input('Digite uma expressão:'))
abre=n.count('(')
fecha=n.count(')')
if abre==fecha:
    print('A sua expressao ta valida!')
else:
    print('A sua expressao está invalida!')