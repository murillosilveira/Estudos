"""Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""


aluno=dict()
aluno['Nome']=str(input('Digite o nome: '))
aluno['Media']=float(input(f'A media do aluno {aluno["Nome"]}: '))
if aluno['Media']>=6:
    aluno['Situacao'] = 'Aprovado'
elif 4<=aluno['Media']<=7:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovado'
print('=-='*15)
for k,v in aluno.items(): #chave e valor
    print(f'{k} é igual a {v}')
"""
temp=dict()
alunos=list()
for k in range(0,2):

    temp['nome']=str(input('Digite o nome: '))
    temp['Nota']=float(input('Digite a nota: '))
    alunos.append(temp.copy())
media=0
for d in alunos:
    for nome,nota in d.items():
        print(f'{nome} e a {nota}')"""


