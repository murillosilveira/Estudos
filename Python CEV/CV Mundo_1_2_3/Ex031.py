#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
n=int(input('Digite a distancia da viagem:'))
if n<=200:
    print('O valor da viagem ficara em {}'.format(0.5*n))
else:
    print('O valor da passagem ficara em {}'.format(0.45*n))