#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
n=int(input('Digite seu ano de nascimento: '))
idade=2022-n

if idade > 18:
    print('Já passou do tempo!')
elif idade ==18:
    print('Parabens, vai servir.')
else:
    print('Você ainda não tem idade suficiente, te faltam {} anos.'.format(18-idade))