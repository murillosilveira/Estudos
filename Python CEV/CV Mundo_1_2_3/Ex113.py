import random as r


op='s'
while op=='s':
    quatnum=int(input('Com quantos números deseja jogar? (entre 6 e 15)'))

    sorteio=list()
    num=0

    for n in range(0,6):
        num = r.randint(1, 60)
        if num in sorteio:
            while num in sorteio:
                num = r.randint(1, 60)
            sorteio.append(num)
        else:
            sorteio.append(num)
        num=100

    sorteio.sort()
    print(sorteio)

    jogo=list()
    temp=list()
    cont=0
    ac0=ac1=ac2=ac3=ac4=ac5=ac6=0

    qtd=int(input("Quantos jogos deseja jogar?"))

    for i in range(1,qtd+1):
        print(f'{i} - ',end='')
        for n in range(0,quatnum):
            num = r.randint(1, 60)
            if num in jogo:
                while num in jogo:
                    num = r.randint(1, 60)
                jogo.append(num)
            else:
                jogo.append(num)
            num=100
        jogo.sort()

        for k in range(0,quatnum):
            if jogo[k] in sorteio:
                cont=cont+1

        temp.append(jogo[:])
        jogo.clear()
        print(f'Jogo: ->{temp}, com {cont} acertos!')
        temp.clear()

        if cont==1:
            ac1+=1
        if cont==2:
            ac2+=1
        if cont==3:
            ac3+=1
        if cont==4:
            ac4+=1
        if cont==5:
            ac5+=1
        if cont==6:
            ac6+=1
        if cont==0:
            ac0+=1
        cont=0

    ac0p=(ac0/qtd)*100
    ac1p=(ac1/qtd)*100
    ac2p=(ac2/qtd)*100
    ac3p=(ac3/qtd)*100
    ac4p=(ac4/qtd)*100
    ac5p=(ac5/qtd)*100
    ac6p=(ac6/qtd)*100


    print('*-*-'*30)
    print(f'Numero de jogos: {qtd}')
    print(f'0 acerto {ac0} - {ac0p:.5f}%')
    print(f'1 acerto {ac1} - {ac1p:.5f}%\n2 acertos {ac2} - {ac2p:.5f}%\n3 acertos {ac3} - {ac3p:.5f}%\n4 acertos {ac4} - {ac4p:.5f}%\n5 acertos {ac5} - {ac5p:.5f}%\n6 acertos {ac6} - {ac6p:.5f}%')
    print('*-*-'*30)


    if quatnum ==6:
        custo=4.50
    elif quatnum==7:
        custo=31.5
    elif quatnum==8:
        custo=126
    elif quatnum==9:
        custo=378
    elif quatnum==10:
        custo=945
    elif quatnum==11:
        custo=2079
    elif quatnum==12:
        custo=4158
    elif quatnum==13:
        custo=7722
    elif quatnum==14:
        custo=13513.5
    elif quatnum==15:
        custo=22522.5

    custototal=(custo*qtd)

    print(f'Você gastaria um total de {custototal}R$ para fazer todas as apostas!')
    receber=(ac4*621.21)+(ac5*28773.28)+(0.35*54575161.62*ac6)
    print(f'Você receberia um total de {receber}R$!')
    print('*-*-' * 30)
    op = str(input('Quer fazer outra análise? [s]'))