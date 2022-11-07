#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

n=str(input('Digite o nome: ')).lower().strip()

contagem=n.count('a')
p=n.find('a')
u=n.find('a',p+1)
print('O nome tem {} tem letras A!\nA primeira aparece na posição {}!\nA segunda na posição {}'.format(contagem,p,u))
