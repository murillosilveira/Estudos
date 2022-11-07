#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random as r

n=int(input('Digite um numero entre 1 e 5 : '))
c=0

while n < 1 or n > 5:
    n=int(input('Digite um numero VALIDO entre 1 e 5 : '))
r=r.randint(1,5)

while n!=r:
    n=int(input('Você errou! Tente novamente: '))
    c=c+1

print('Parabéns você acertou, o número era {}! Você fez {} tentativas!'.format(n,c+1))