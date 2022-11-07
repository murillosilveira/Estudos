"""Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado."""
import random as r
from operator import itemgetter

dicionario={'jogador 1':r.randint(1,6),
            'jogador 2':r.randint(1,6),
            'jogador 3':r.randint(1,6),
            'jogador 4':r.randint(1,6)}

ranking=dict()
ranking=sorted(dicionario.items(),key=itemgetter(1),reverse=True)


for i,v in enumerate(ranking):
    print(f'O jogador {v[0]} tirou: {v[1]}')



