Primeiros comandos em python
Todos os comando são funções, portanto devem ter ()

print('ola mundo!') -> com aspas simples
print(4) números

*Variáveis:
//Toda variável é um objeto
ex:
Nome = 'Murillo'

*Criando interatividade com usuário:
INPUT

nome = input('Qual é o seu nome?')










------> Ex 002<------
#Exercício Python 2: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

n=input(str('Digite o seu nome: '))
print('Boas vindas {}!'.format(n))
---------------------








TIPOS PRIMITIVOS
n1=int(input('Digite um numero:'))
n2=int(input('Digite outro número:'))
s=n1+n2
print('A soma do número {} com o número {} vale{}!'.format(n1,n2,s))

int - inteiro
float - ponto flutuante / numero real
bool - booleano (true ou false)
str - string










------> Ex 003<------
#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
s=n1+n2
print('A soma do númerp {} com o número {} vale {}!'.format(n1,n2,s))
print(f'a soma do número {n1} com {n2} da {s}!')
----------------------
------> Ex 004<------
#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n1=input('Digite algo:')

print('O tipo primitivo é {}!'.format(type(n1)))
print('Tem apenas espaços?',n1.isspace()) #detecta se tem espaço
print('É um número?', n1.isnumeric())
print('É alfabetico? (tem apenas letras)',n1.isalpha())
print('É alfanumérico? (letras e numeros)',n1.isalnum())
print('Está em maiusculas?',n1.isupper())
print('Está em maiusculas?',n1.islower())
print('Está capitalizada? (primeira letra maiuscula)',n1.istitle())

O n1 seria o OBJETO, todo o objeto tem CARACTERÍSTICAS e realiza FUNCIONALIDADES, tendo ATRIBUTOS e MÉTODOS.
Como colocamos o () depois estamos trabalhando com MÉTODOS.
----------------------











OPERACOES ARITIMETICAS

ADICAO  +
SUBTRACAO  -
MULTIPLICACAO  *
DIVISAO  /
POTÊNCIA  ** OU POW(4,3)=64
DIVISAO INTEIRA  //
RESTO DA DIVISAO  %

ORDEM DE PROCEDENCIA
1- ()
2- **
3- *   /    //    %
4- + -

EX: 5 + 3 * 2 = 11
'OI' * 5 = OIOIOIOIOI

FORMATACAO DO {} 
print('murillo{:20}!') = murillo           !
print('murillo{:>20}!') =           murillo!
print('murillo{:^20}!') =      murillo     !
print('murillo{:-^20}!') =------murillo-----!
print('3.13394343{:.2F}!') =3.13! #duas casas flutuantes

NÃO FAZER A QUEBRA DE LINHA end=''
print('testando a quebra de linha',end='')
QUEBRA DE LINHA
print('testando a quebra\n de linha')











------> Ex 005<------
#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
N=int(input('Digite um número inteiro: '))
print('O número digitado foi: {}!\nSeu atecessor é {}!\nSeu Sucessor é {}!'.format(N,N-1,N+1))
----------------------
------> Ex 006<------
#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=float(input('Digite um número: '))
print('O dobro é {}, o triplo é {} e a raíz quadrada é {:.2f}!'.format(n*2,n*3,n**(1/2)))
----------------------
------> Ex 007<------
#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print('A média foi {:.2f}'.format(m))
----------------------
------> Ex 008<------
#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n=float(input('Digite um número em metros'))
print('O numero digitado tem {} centímetros e {} milimetros!'.format(n*100,n*1000))
----------------------
------> Ex 009<------
#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n=int(input('Digite um número: '))
print('*'*15)
print('{} x 1 = {}'.format(n,n*1))
print('{} x 1 = {}'.format(n,n*2))
print('{} x 1 = {}'.format(n,n*3))
print('{} x 1 = {}'.format(n,n*4))
print('{} x 1 = {}'.format(n,n*5))
print('{} x 1 = {}'.format(n,n*6))
print('{} x 1 = {}'.format(n,n*7))
print('{} x 1 = {}'.format(n,n*8))
print('{} x 1 = {}'.format(n,n*9))
print('{} x 1 = {}'.format(n,n*10))
print('*'*15)
----------------------
------> Ex 0010<------
#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n=float(input('Digite a quantidade de dinheiro: '))
print('Você tem {:.0f} reais, equivalentes a {:.2f} dolares!'.format(n,n/5.19))
----------------------
------> Ex 0011<------
#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
a=int(input('Digite a altura: '))
l=int(input('Digite a largura: '))
print('A parede tem uma área de {}m², serão necessarias {:.0f} latas de tintas'.format(l*a,(l*a)/2))
----------------------
------> Ex 0012<------
#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n=float(input('Digite o preço do produto: '))
print('O produto com desconto fica em {:.2f}$'.format(n*0.95))
----------------------
------> Ex 0013<------
#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n=float(input('Digite o salario: '))
print('O salario com aumento fica em {:.2f}$'.format(n*1.15))
----------------------
------> Ex 0014<------
#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c=float(input('Digite a temperatura em celsius:'))
f=((9/5)*c)+32
print('A temperatura é {:.2f}F'.format(f))
----------------------
------> Ex 0015<------
#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km=int(input('Digite a quantidade de km:'))
d=int(input('Digite a quantidade de dias'))
custo=(60*d)+ (0.15*km)
print('O custo total ficou em {:.2f}$'.format(custo))
----------------------








USANDO MÓDULOS NO PYTHON

import bebidas #importa todas as bebidas
import doces #importa todas os doces

from bebidas import agua
from doces import pudim

Biblioteca MATH
Ceil = arrendodamento pra cima.
Floor = arrendondamento pra baixo.
Truncate = truncar (Elimina deppois da vírgula)
Sqrt = raiz quadrada
Factorial = fatorial



















------> Ex 0016<------
#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n=float(input('Digite um número: '))
print('A porção inteira do número é: {}!'.format(trunc(n)))
----------------------
------> Ex 0017<------
#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math as m
ca=float(input('Digite o Cateto Adjacente: '))
co=float(input('Digite o Cateto Oposto: '))
h=m.sqrt(pow(ca,2)+pow(co,2))
print('A hipotenusa é {:.2f}'.format(h))
----------------------
------> Ex 0018<------
#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math as m
n=m.radians(int(input('Digite o Angulo: ')))
print('O valor do seno é {:.2f}\nDo Cosseno é {:.2f}\nDa tangente é {:.2f}'.format(m.sin(n),m.cos(n),m.tan(n)))
----------------------
------> Ex 0019<------
#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random as r
n1=str(input('Aluno 1:'))
n2=str(input('Aluno 2:'))
n3=str(input('Aluno 3:'))
n4=str(input('Aluno 4:'))
n=[n1,n2,n3,n4]
s=n[r.randint(0,3)]#poderiamos usar o comando r.choice(n)
print('O aluno sorteado foi {}!'.format(s))
----------------------
------> Ex 0020<------
#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random as r
n1=str(input('Aluno 1:'))
n2=str(input('Aluno 2:'))
n3=str(input('Aluno 3:'))
n4=str(input('Aluno 4:'))
n=[n1,n2,n3,n4]
s=r.sample(n,4)
print('A ordem de apresentação será {}!'.format(s))
----------------------
------> Ex 0021<------
#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
----------------------



















MANIPULAÇÃO DE TEXTO

frase="CURSO EM VIDEO PYTHON"
frase=[9:13] -> VIDEO #O ultimo Valor não entra na contagem!
frase=[9:13:2] -> VDO #Pula de 2 em 2
frase=[:5] -> CURSO #Começa do inicio
frase=[15:] -> PYTHON

ANÁLSIE STRING
len(frase) = 21 #Retorna a quantidade de caracteres!
frase.count('o') = 3 #Retorna a quantidade de vezes que o 'o' aparece!
frase.find('deo') = 11 #Retorna a posição que a estrutura 'deo' começou.
'Curso' in frase = True #Existe curso em frase?

TRANSFORMACAO
frase.replace('Python','Android') = CURSO EM VIDEO ANDROID.format
frase.upper() = Maiusculo
frase.lower() = Minusculo
frase.captalize() = Curso em vídeo #apenas primeiro caractere maiusculo.
frase.tittle() = Curso Em Video #primeiro caractere de cada palavra maiusculo
frase.strip() = #remove todos os espações inuteis no começo e no final da String.
	frase.rstrip() = #strip a direita.
	fease.lstrip() = #strip a esquerda.

DIVISAO
frase.split() = #Divide uma lista onde cada elemento é separado por seu splitador (espaço)
'-'.join(frase) = Curso-Em-Video





















------> Ex 0022<------
# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome: '))
sep=nome.split()
join=''.join(sep)
print('Seu nome é: {}!'.format(nome.upper()))
print('O nome tem {} letras e o primeiro nome tem {} letras.'.format(len(join),len(sep[0])))
----------------------
------> Ex 0023<------
#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
import random as r
aleat=r.randint(0,9999)
st=str(aleat)
print('o número digitado foi {}!\nMilhar {}!\nCentena {}!\nDezena {}!\nUnidade {}!'.format(st,st[0],st[1],st[2],st[3]))
----------------------
------> Ex 0024<------
#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
frase=str(input('Digite o nome da cidade: ')).strip().lower()
v='santo' in frase
print('Existe Santo no nome da cidade? {}!'.format(v))
----------------------
------> Ex 0025<------
#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
frase=str(input('Digite o nome da cidade: ')).strip().lower()

v='santo' in frase
print('Existe Santo no nome da cidade? {}!'.format(v))
----------------------
------> Ex 0026<------
#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
frase=str(input('Digite o nome: ')).strip().lower()

v='silva' in frase
print('Existe silva no nome? {}!'.format(v))
----------------------
------> Ex 0027<------
#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome=str(input('Digite seu nome completo: ')).split()
qtd=len(nome)
print('O primerio nome é {}!\nO ultimo nome é {}!'.format(nome[0],nome[len(nome)-1]))
----------------------














CONDICIONAIS
if carro.esquerda():
	Bloco True
else:
	Bloco False















------> Ex 0028<------
#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random as r


n=int(input('Digite um valor entre 0 e 5: '))

p=r.randint(0,5)
print('O número digitado foi {} e o número sorteado foi {}!'.format(n,p))
if n==p:
    print('Parabéns, você venceu!')
else:
    print('Parabéns, você perdeu!')

----------------------
------> Ex 0029<------
#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
n=int(input('Digite a velocidade do carro: '))

if n>80:
    print('Você se fodeu e foi multado em {}R$'.format((n-80)*7))
else:
    print('Motorista conciente')
----------------------
------> Ex 0030<------
#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
n=int(input('Digite um número: '))
r=n%2
if r==0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar!'.format(n))
----------------------
------> Ex 0031<------
#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
n=int(input('Digite a distancia da viagem:'))
if n<=200:
    print('O valor da viagem ficara em {}'.format(0.5*n))
else:
    print('O valor da passagem ficara em {}'.format(0.45*n))
----------------------
------> Ex 0032<------
#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
----------------------
------> Ex 0033<------
#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))
if n1>n2:
    if n1>n3:
        maior=n1
        if n2<n3:
            menor=n2
        else:
            menor=n3
    else:
        maior=n3
        if n1<n2:
            menor=n1
        else:
            menor=n2
else:
    if n2>n3:
        maior=n2
    else:
        maior=n3
    if n1<n3:
        menor=n1
    else:
        menor=n3
print('O maior número foi {}!'.format(maior))
print('O menor número foi {}!'.format(menor))

----------------------
------> Ex 0034<------
#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n=float(input('Digite o salário: '))

if n>1250:
    print('O salário foi de {:.2f}R$'.format(n*1.1))
else:
    print('O salário foi de {:.2f}R$'.format(n*1.15))
----------------------
------> Ex 0035<------
#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))

maior=max(n1,n2,n3)
menor=min(n1,n2,n3)
meio=(n1+n2+n3)-(maior+menor)

if menor+meio>=maior:
    print('É possível')
else:
    print('Não é possível')
----------------------















CORES PYTHON
PADRÃO ANSI
#\O33[(estilo: texto:background)m
#\O33[(0: 33:44)m
estilo:
0 - nenhum
1 - negrito
4 - sublinhado
7 - invertido

cor texto/fundo:		
30/40 - branco
31/41 - vermelho
32/42 - verde
33/43 - amarelo
34/44 - azul
35/45 - lilas
36/46 - ciano
37/47 - cinza

CONDICOES ANINHADAS
if carro.siga():
	em frente
elif carro.direita():
	vira direita
else:
	vira esquerda





















------> Ex 0036<------
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
n1=int(input('Digite o valor da casa: '))
n2=int(input('Digite o valor do salario: '))
n3=int(input('Digite os anos de pagamento:'))
prest=(n1/(n3*12))


if prest < n2:
    print('O valor total a ser pago será de {:.2f}R$!'.format(prest))
else:
    print('Emprestimo negado!')
----------------------
------> Ex 0037<------
#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n=int(input('Digite um número inteiro: '))

bin=bin(n)
oct=oct(n)
hex=hex(n)

x=int(input('Você deseja converter o número {} para qual base? bin[1] oct[2] ou hex[3]:'.format(n)))
if x==1:
    print(bin)
elif x==2:
    print(oct)
else:
    print(hex)
----------------------
------> Ex 0038<------
#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))

if n1>n2:
    print('O primeiro valor é maior.')
elif n1==n2:
    print('Os valores sao iguais')
else:
    print('O segundo é maior.')
----------------------
------> Ex 0039<------
#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
n=int(input('Digite seu ano de nascimento: '))
idade=2022-n

if idade > 18:
    print('Já passou do tempo!')
elif idade ==18:
    print('Parabens, vai servir.')
else:
    print('Você ainda não tem idade suficiente, te faltam {} anos.'.format(18-idade))
----------------------
------> Ex 0040<------
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

----------------------
------> Ex 0041<------
#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
----------------------
------> Ex 0042<------
"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

n1=int(input('Digite um valor:'))
n2=int(input('Digite um valor:'))
n3=int(input('Digite um valor:'))

maior=max(n1,n2,n3)
menor=min(n1,n2,n3)
meio=(n1+n2+n3)-(maior+menor)

if menor+meio>=maior:
    print('É possível')

    if n1==n2 and n1==n3:
        print('Equilátero')
    elif n1!=n2 and n2!=n3:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não é possível')
----------------------
------> Ex 0043<------
"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida"""
----------------------
------> Ex 0044<------
""""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros"""
----------------------
------> Ex 0045<------
#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
----------------------












LAÇOS
for c in range(0,3,1): Começa em 1, vai até o 3 e tem o passo de 1.
	if restricao();

for c in range(0,10):
    print(c)
    c=c+1





















------> Ex 0046<------
#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time as t

for c in range(9,0,-1):
    print(c)
    t.sleep(1)
print('poww!!!!')
----------------------
------> Ex 0047<------
#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(1,51):
    if c%2==0:
        print(c)
----------------------
------> Ex 0048<------
#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s=0
for c in range(3,501,3):
    if c%2==1:
        s=s+c
print(s)
----------------------
------> Ex 0049<------
#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n=int(input('Digite um número para tabuada: '))

for c in range(1,10):
    print('{} X {} = {}'.format(n,c,n*c))
----------------------
------> Ex 0050<------
#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
import random as r
soma=0
for c in range(1,7):
    n=r.randint(1,50)
    if  n%2==0:
        soma+=n
        print(n)
print(f'A soma deu {soma}')
----------------------
------> Ex 0051<------
#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão da PA: '))
s=0
for c in range(n,n+10*r,r):
    print(c,end='->')
    s+=1
print('A soma deu {}!'.format(s))
----------------------
------> Ex 0052<------
#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n=int(input('Digite um numero: '))
s=0
for c in range(2,n):
    if n%c==0:
        s+=1
if s==0:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
----------------------
------> Ex 0053<------
#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
n=str(input('Digite uma frase: ')).lower().strip().replace(' ','')

y=len(n)-1
x=0
c=0
print(n)
for c in range(len(n),0,-1):
    if n[x]==n[y]:
    else:
        c+=1
    x+=1
    y-=1
if c>1:
    print(c)
    print('Não é um palindromo')
else:
    print(c)
    print('É um palindromo')
----------------------
------> Ex 0054<------
#Exercício Python 54: Crie um programa que leia o ano de nascimento de duas pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

x=0
y=0

for c in range(0,3):
    n=int(input('Digite o ano de nascimento: '))
    if (2022-n)<18:
        x+=1
    else:
        y+=1
print('Ao todo {} maiores de idade e {} menores.'.format(y,x))
----------------------
------> Ex 0055<------
#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior=0
menor=10000000

for c in range(1,6):
    n=int(input('Digite o peso da pessoa {}:'.format(c)))
    if n > maior:
        maior=n
    if n < menor:
        menor=n
print('O maior peso foi {} e o menor foi {}'.format(maior,menor))
----------------------
------> Ex 0056<------
#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
----------------------










ESTRUTURA DE REPETIÇÃO while 


C=1
while c < 10:
	print(c)
	c=c+1
print('fim')
















------> Ex 0057<------
#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s='g'
while s not in 'MmFf':
    s=str(input('Por favor, digite o sexo [f] ou [m]'))
print('obrigado!')
----------------------
------> Ex 0058<------
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
----------------------
------> Ex 0059<------
"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso."""


n=float(input('Digite um valor: '))
m=float(input('Digite outro valor: '))

c=int(input('[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números,[ 5 ] sair do programa)'))
while c > 0 and c < 5:

    if c==1:
        print('O resultado é {}!'.format(m+n))
    elif c==2:
        print('O resultado é {}!'.format(m * n))
    elif c==3:
        print('O resultado é {}!'.format(max(m,n)))
    elif c==4:
        n = float(input('Digite um valor: '))
        m = float(input('Digite outro valor: '))
    c=int(input('[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números,[ 5 ] sair do programa)'))
----------------------
------> Ex 0060<------
"""Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:"""

import math as m

n=int(input('Digite um numero:'))

print('O fatorial desse número é: {}!'.format(m.factorial(n)))
f=1
while n >= 2:
    f=f*n
    n=n-1
print('O fatorial desse número é: {}!'.format(f))
----------------------
------> Ex 0061<------
"""Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."
"""

razao=int(input('Digite a razao da P.A:'))
a=int(input('Digite o primeiro termo da P.A:'))
result=a
c=1

while c <11:
    print(result,end='->')
    result=result+razao
    c+=1
print('fim')
----------------------
------> Ex 0062<------
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
----------------------
------> Ex 0063<------
"""Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8"""

n=int(input('Digite os termos para sequencia de fibonacci: '))
atual=0
prim=0
seg=0
a=0
c=0
while c<=n:
    seg=prim
    prim=atual

    print(atual,end='->')
    atual=prim+seg
    if atual==0:
        atual=1
    c=c+1
print('fim')
----------------------
------> Ex 0064<------
"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
o final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
n=0
total=0
c=0
while n!=999:
    n=int(input('Digite um valor: '))
    total=total+n
    c+=1
print('Você digitou {} valores, o total foi de {}.'.format(c,total))
----------------------
------> Ex 0065<------
"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
----------------------
















INTERROMPENDO REPETIÇÕES COM WHILE:

while c<10:
	print(c)
	break#interrompe
	c+=1













------> Ex 0066<------
"""Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag)."""

n=0
total=0
c=0
while n!=999:
    n=int(input('Digite um valor: '))
    total=total+n
    c+=1
print('Você digitou {} valores, o total foi de {}.'.format(c,total))
----------------------
------> Ex 0067<------
"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""

n=int(input('Digite um numero:'))
m=1
while n>=0 and m<12:
    print('{} x {} = {}'.format(n,m,n*m))

    m+=1
    if m==11:
        m=1
        n = int(input('Digite um numero:'))
----------------------
------> Ex 0068<------
#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
----------------------
------> Ex 0069<------
"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos."""
----------------------
------> Ex 0070<------
"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato."""
----------------------
------> Ex 0071<------
"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
----------------------













----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TUPLAS (VARIÁVEIS COMPOSTAS)

*AS TUPLAS SAO IMUTAVEIS*
lanche=('hamburger','pizza','suco','pudim')
for pos, comida in enumerate(lanche):
	print(f'eu vou comer {comida} na pos {pos}')

SORTED = print(sorted(lanche)) #Lanche ordenado de forma alfabetica
a=(1,2,3,4)
b=(5,8,1,2)
c=a+b
print(c) ->(1,2,3,4,5,8,1,2)
print(c.count(5)) = 1 vez
print(c.index(8)) = 5 # Informa a posição
















------> Ex 0072<------
"""Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de
zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 5) e mostrá-lo por extenso."""


nome=('zero','um','dois','tres','quatro','cinco')
n=int(input('Digite um número: '))

while n < 0 or n > 5:
    n = int(input('Digite um número válido: '))
    while n >=0 and n <6:
        print(f'O número digitado foi {nome[n]}')
        break

----------------------
------> Ex 0073<------
"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""
----------------------
------> Ex 0074<------
"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

import random as r

lista=(r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100),r.randint(1,100))

maior=max(lista)
menor=min(lista)

print(sorted(lista))
print(f'Maior = {maior}')
print(f'Menor = {menor}')
----------------------
------> Ex 0075<------
"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
n4=int(input('Digite um número: '))
lista=(n1,n2,n3,n4)

print('O número 9 apareceu {} vezes.'.format(lista.count(9)))
if 3 not in lista:
    print('Não tem numero 3.')
else:
    print('O primeiro valor 3 foi digitado na {} posição.'.format(lista.index(3)))
print('Os números pares são: ',end='')
for c in range(0,len(lista)):
    if lista[c]%2==0:
        print('{} '.format(lista[c]),end=' ')
----------------------
------> Ex 0076<------
"""Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
----------------------
------> Ex 0077<------
"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

lista=('murillo','mercado','tati','auro')

for c in range(0,len(lista)):
    print('As vogais da palavra {} são: '.format(lista[c]),end='')
    str=lista[c]
    for d in range(0,len(str)):
        if str[d] in 'aeiouAEIOU':
            print(str[d],end='')
    print('')
----------------------















LISTAS
INSRIR ELEMENTOS
lanhce=[1,2,3,4,5]
lanche.append('3') -> adiciona um elemento no final
lanche.insert(0,'x') -> adiciona um valor na posicao 0
APAGAR ELEMENTOS
del lance [3]
lanche.pop(3)
lanche.remove('pizza') #remove o valor que quero eliminar, apenas a primeira ocorrencia
CRIAR LISTA
valores=lista(range(4,11))
valores.sort() -> ordena os valroes
valores.sort(reverse=true) -> ordena de forma descrescente
OBS:
valores=[1,2,3,4]
for c,v in enumerate(valores): #o enumerate pega tanto a chave quanto o valor
	print(f'na posição {c} encontrei o valor {v}') = Não posicao 0 encontrei o valor 5....

#Ao igualarmos uma lista em outra o python cria uma ligação entre elas.













------> Ex 0078<------
"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

lista=[]

for valor in range(0,5):
    lista.append(int(input('Digite um valor:')))
for pos,valores in enumerate(lista):
    if valores==max(lista):
        print('O maior valor foi {} na posicao {}'.format(max(lista),pos))
    if valores == min(lista):
        print('O menor valor foi {} na posicao {}'.format(min(lista), pos))
----------------------
------> Ex 0079<------
"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
 lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
  digitados, em ordem crescente."""

lista=[]

for c in range(0,5):
    n=int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)

lista.sort()
print('A lista digitada em ordem foi: ',end='')
for pos,d in enumerate(lista):
    print(d,end=' ')
----------------------
------> Ex 0080<------
"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""

lista=[0]
m=0
for c in range(0,7):
    n=int(input('Digite um valor: '))
    for m in range(0,len(lista)):
        if n > lista[m]:
            pos=len(lista)
        else:
            pos = lista.index(lista[m])
            break
    m=m+1
    lista.insert(pos,n)
lista.remove(0)
print(lista)
----------------------
------> Ex 0081<------
"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

n='s'
lista=[]
count=0
while n not in 'Nn':
    f=int(input('Digite um valor: '))
    n=str(input('Quer continuar? [N] para sair'))
    count+=1
    lista.append(f)
print(f'Foram digitados {count} valores.')
lista.sort(reverse=True)
print(f'A lista de valores digitados foi: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
----------------------
------> Ex 0082<------
"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas."""

import random as r

lista=[]
lista_par=[]
lista_impar=[]

termos=int(input('Digite a quantidade de termos: '))

for c in range(0,termos):
    n=r.randint(0,99)
    lista.append(n)
    if n%2==0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'lista:{lista}')
print(f'lista par:{lista_par}')
print(f'lista impar:{lista_impar}')
----------------------
------> Ex 0083<------
"""Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
eu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

lista=[]

n=str(input('Digite uma expressão:'))
abre=n.count('(')
fecha=n.count(')')
if abre==fecha:
    print('A sua expressao ta valida!')
else:
    print('A sua expressao está invalida!')
----------------------









LSITAS COMPOSTAS

PESSOAS=[['PEDRO',25],['MARIA',19]]
print(PESSOAS[0][0]) = 'PEDRO'
print(PESSOAS[[1][1]])= 19
print(PESSOAS[1]) = ['PEDRO',25]

lista1=['murillo',19]

lista2=[]
lista2.append(lista1[:]) # faz a cópia
lista1[0]='jose'
lista1[1]=2
print(lista2)

lista=[[1,2],[3,4],[5,6],[7,8]]

for i in lista:
    print(i[0]) # retorna 1,3,5,7
 EXCLUIR LISTA
lista.clear()













------> Ex 0084<------
"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

lista=[['murillo',75],['auro',78],['tati',65]]
c=0
#for n in range(0,4):
    #pessoa=str(input('Digite o nome da pessoa:'))
    #peso=int(input('Digite o peso:'))
    #lista.append([pessoa,peso])
    #c+=1


max=0
min=100000000
print(lista)

for i in lista:
    if i[1]>max:
        max=i[1]
    if i[1]<min:
        min=i[1]

print(f'A pessoa mais pesada pesa {max} e a mais leve pesa {min}!')
----------------------
------> Ex 0085<------
"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
 lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
 em ordem crescente."""

import random as r

temp=[]
lista=[[],[]]


qtd=int(input('Digite a quantidade de pessoas:'))

for c in range(0,qtd):
    x=r.randint(0,100)
    if x%2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

print(lista)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares foram: {lista[0]}')
print(f' e os numeros impares foram: {lista[1]}',end='')
----------------------
------> Ex 0086<------
"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo
teclado. No final, mostre a matriz na tela, com a formatação correta."""

matriz=[[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        x=int(input('Digite um numero:'))
        matriz[i].append(x)
for m in range(0,3):
    print(matriz[m])

----------------------
------> Ex 0087<------
"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz=[[],[],[]]
soma=0
terceira=0

for i in range(0,3):
    for j in range(0,3):
        x=int(input('Digite um numero:'))
        matriz[i].append(x)
        if x%2==0:
            soma=soma+x
        if j==2:
            terceira=terceira+x
for m in range(0,3):
    print(matriz[m])

seg=max(matriz[1])
print(f'A soma de todos os valores pares digitados foi: {soma}')
print(f'A soma de todos os valores da 3 coluna foi: {terceira}')
print(f'O maior valor da 2 linha foi: {seg}')
----------------------
------> Ex 0088<------
"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""

import random as r

n=int(input('Digite a quantidade de jogos: '))
temp=list()
lista=list()

for c in range(0,n):
    for i in range(0,6):
        x=r.randint(1,60)
        temp.append(x)
        lista.append(temp[:])
        temp.clear()
        lista.sort()
    print(f'Jogo {c+1} -> {lista}')
    lista.clear()
----------------------
------> Ex 0089<------
"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário
  possa mostrar as notas de cada aluno individualmente."""
----------------------












DICIONARIOS
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

dados={}
dados=dict()

INSERIR VALORES
dados={'nome':'pedro','idade':25} #elementos são chamados de keys ou chaves
dados['sexo']='M'

VALORES X INTES X CHAVES
filme={'titulo':'starwars','ano':1977,'diretor':'george lucas'}
print(filme.values()) -> vai me retornar todos os valores = starwars,1977,george lucas
print(filme.keys()) --> vai me retornar todos As chaves = titulo,ano,diretor
print(filme.itens()) --> vai me retornar todos os valores/chaves
for k,v in filme.itens():
	print(f'O{k} é {v}')


REMOVER ELEMENTOS
del dados['idade']

para copiar:
brasil.append(estado.copy())

ORDENRAR
from operator import itemgetter
ranking=dict()
ranking=sorted(dicionario.items(),key=itemgetter(1),reverse=True)

















------> Ex 0090<------
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
----------------------
------> Ex 0091<------
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
----------------------
------> Ex 0092<------
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

----------------------
------> Ex 0093<------
"""Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
 gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
  de gols feitos durante o campeonato."""
----------------------
------> Ex 0094<------
"""Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
 guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
  No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista 
  com as mulheres D) Uma lista de pessoas com idade acima da média"""
----------------------







FUNCOES (DEF)

def mostralinha():
	print('--------------------')


PARAMETROS!!!
def linha(msg): 
	print('-'*30)
	print(msg)
	print('-' * 30)

linha('Titulo foda')

DESEMPACOTAR PARAMETROS
def contador(*num):
	for valor in num:
		print(f'{valor} ',end='')

contador(2,1,7)
contador(1,2)
contador(1,4,6,7,8,9)














----------------------
------> Ex 0096<------
"""Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno."""

def area(altura,largura):
    print('O terreno tem uma largura {} e uma altura {}. Sua área é {}m²!'.format(largura,altura,largura*altura))

print(area(5,89))

----------------------
------> Ex 0097<------
"""Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.      """

def text(msg):
    print('-'*len(msg))
    print(msg)
    print('-' * len(msg))
text('oiiiiiiiiii')
----------------------
------> Ex 0098<------
"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
fim e passo. Seu programa tem que realizar três contagens através da função criada:
 a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

import time

def contador(inicio,fim,passo):

    while inicio<fim+1:
        print(inicio,end= '-')
        time.sleep(1)
        inicio=inicio+passo

x=int(input('Digite o inicio: '))
y=int(input('Digite o fim: '))
z=int(input('Digite o passo: '))

print(contador(x,y,z))
----------------------
------> Ex 0099<------
"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""


def grande(*num):
    max = 0
    for valor in num:
        if valor > max:
            max=valor
    print(max)

grande(2,3,4,1,3,4,6,7,1,2,13,5,53,2)
----------------------
------> Ex 00100<------
"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""

import random as r

temp = list()
lista2=list()

def somapar(*num):
    soma=0
    for valor in num:
        if valor %2==0:
            soma=soma+valor
    print(soma)


def sorteia(n):

    lista=list()
    for c in range (0,n):
        lista.append(r.randint(1,10))
    print(lista)


print(f'Os números sorteados foram:',end='')
temp=sorteia(5)
temp

----------------------





DOCSTRING
def contador(x,y):
	"""aqui é exatamente a minha docstring"""
PARAMETROS OPICIONAIS

def contador(a,b,c=0): # c é opicional

ESCOPO DE VARIAVEIS
->Variavel local = x-> funciona dentro da definicao
->Variavel globaI = x-> funciona em todos os locais.

RETORNO DE VALORES
import random as r

def aleat(x,y):
    s=r.randint(x,y)
    return s

r1=aleat(1,2)
r2=aleat(3,4)
r3=aleat(5,6)

print(r1)
print(r3)
print(r2)

2
5
4







------> Ex 00101<------
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
----------------------
------> Ex 00102<------
"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial."""

def fatorial(x,c=0):
    if c==1:
        s=x
        p=0
        for c in range(0,x-1):
            p=s*(x-1)
            print(f'{s}x{(x-1)}={p}')
            s=p
            x=x-1
    elif c==0:
        s=x
        p=0
        for c in range(0,x-1):
            p=s*(x-1)
            s=p
            x=x-1
        print(p)
----------------------
------> Ex 00103<------
"""Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
 algum dado não tenha sido informado corretamente."""
----------------------
------> Ex 00104<------
"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a 
função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)"""
----------------------
------> Ex 00105<------
"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota– A média da turma– A situação (opcional)"""
----------------------
------> Ex 00106<------
"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""
----------------------









MODULOS E PACOTES:
MODULOS:
Os modulos nada mais são que conjuntos de funcoes!
São separados em um local distinto, tem como beneficio reduzir o tamanho do nosso código.
PACOTES:
São um conjunto de módulos separados por assuntos.
















------> Ex 00107<------
"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""
----------------------
------> Ex 00108<------
"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado."""
----------------------
------> Ex 00109<------
"""Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""
----------------------
------> Ex 00110<------
"""Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre 
na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""
----------------------
------> Ex 00111<------
"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""
----------------------
------> Ex 00112<------
"""Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma 
função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar 
apenas valores que seja monetários."""
----------------------




TRATAMENTO DE ERROS:
n=int(input('Digite um valor:'))

try:
    r=1/n
except Exception as erro:
    print(f'Erro {erro.__class__}')
else:
    print('ok')
finally:
    print('Volte sempre')




------> Ex 00113<------
----------------------
------> Ex 00114<------
----------------------
------> Ex 00115<------
----------------------
