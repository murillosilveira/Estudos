#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))

m=(n1+n2)/2
print('Sua média foi {}'.format(m),end='->>')
if m>=7:
    print('Parabens aprovado!')
elif m>=5 and m <7:
    print('Recuperação')
else:
    print('Reprovado')