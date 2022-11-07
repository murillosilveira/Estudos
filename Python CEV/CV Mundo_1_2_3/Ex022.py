# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome: '))
sep=nome.split()
join=''.join(sep)
print('Seu nome é: {}!'.format(nome.upper()))
print('O nome tem {} letras e o primeiro nome tem {} letras.'.format(len(join),len(sep[0])))