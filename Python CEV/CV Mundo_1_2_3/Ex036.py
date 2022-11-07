#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
n1=int(input('Digite o valor da casa: '))
n2=int(input('Digite o valor do salario: '))
n3=int(input('Digite os anos de pagamento:'))
prest=(n1/(n3*12))


if prest < n2:
    print('O valor total a ser pago será de {:.2f}R$!'.format(prest))
else:
    print('Emprestimo negado!')