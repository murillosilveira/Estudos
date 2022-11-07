"""Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

Nome= str(input('Digite o nome:'))
AnoNasc=int(input('Digite o Ano de nascimento: '))
cart=int(input('Digite a carteira de trabalho:[0] para nao tem'))
if cart!=0:
    AnoTrab=int(input('Digite o Ano de trabalho: '))
    sal=float(input('Digite o salário: '))
    idadeApos = AnoTrab + 40 - AnoNasc
else:
    AnoTrab=0
    sal=0
    idadeApos = 0
idade=2022-AnoNasc


dici = {"Nome":Nome,
        "Ano Nasci":AnoNasc,
        "Num.Cart":cart,
        "idade":idade,
        "Ano trab":AnoTrab,
        "Salario":sal,
        "Idade Apos":idadeApos
       }
for k,v in dici.items():
    print(f'{k} é {v}')
