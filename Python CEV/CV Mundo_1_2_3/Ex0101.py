"""Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
 OBRIGATÓRIO nas eleições."""

def voto(ano):
    idade=2022-ano
    if idade > 18:
        x='Apto'
    elif 16<=idade<=18:
        x='Opcional'
    else:
        x='Negado'
    return x


status=voto(2010)
print('O usuario esta {}'.format(status))



