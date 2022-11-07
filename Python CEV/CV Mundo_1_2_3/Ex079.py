"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
 lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
  digitados, em ordem crescente."""

lista=[]

for c in range(0,5):
    n=int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)

lista.sort()
print('A lista digitada em ordem foi: ',end='')
for pos,d in enumerate(lista):
    print(d,end=' ')



