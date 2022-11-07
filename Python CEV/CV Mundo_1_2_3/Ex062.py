"""Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

razao=int(input('Digite a razao da P.A:'))
a=int(input('Digite o primeiro termo da P.A:'))
result=a
c=1
count=2

termos=10+1


while count != 0:
    while c <termos:
        print(result,end='->')
        result=result+razao
        c+=1
    count=int(input('Você quer mostrar mais quantos termos? [0] para sair!'))
    while c<count+termos:
        print(result,end='->')
        result=result+razao
        c+=1
    termos=count+termos