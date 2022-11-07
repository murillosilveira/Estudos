#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
n=str(input('Digite uma frase: ')).lower().strip().replace(' ','')

y=len(n)-1
x=0
c=0
print(n)
for c in range(len(n),0,-1):
    if n[x]==n[y]:
    else:
        c+=1
    x+=1
    y-=1
if c>1:
    print(c)
    print('Não é um palindromo')
else:
    print(c)
    print('É um palindromo')