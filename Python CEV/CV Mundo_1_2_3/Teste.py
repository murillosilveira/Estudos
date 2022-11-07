x1=x2=x3=x4=x5=x6=x7=x8=x9=x10=0
y1=y2=y3=y4=y5=y6=y7=y8=y9='-'
import random as r

m=1
n=2
randoml=r.randint(1,3)


while m==1:

    """print(f'{x7}  {x8}  {x9}')
    print(f'{x4}  {x5}  {x6}')
    print(f'{x1}  {x2}  {x3}')"""






    if x1==1:
        y1='X'
    if x2==1:
        y2='X'
    if x3==1:
        y3='X'
    if x4==1:
        y4='X'
    if x5==1:
        y5='X'
    if x6==1:
        y6='X'
    if x7==1:
        y7='X'
    if x8==1:
        y8='X'
    if x9==1:
        y9='X'

    if x1==4:
        y1='O'
    if x2==4:
        y2='O'
    if x3==4:
        y3='O'
    if x4==4:
        y4='O'
    if x5==4:
        y5='O'
    if x6==4:
        y6='O'
    if x7==4:
        y7='O'
    if x8==4:
        y8='O'
    if x9==4:
        y9='O'

    print(f'{y7}  {y8}  {y9}')
    print(f'{y4}  {y5}  {y6}')
    print(f'{y1}  {y2}  {y3}')





    valid1=3
    if x1+x2+x3==valid1 or x4+x5+x6==valid1 or x7+x8+x9==valid1 or x1+x4+x7==valid1 or x2+x5+x8==valid1 or x3+x6+x9==valid1 or x1+x5+x9==valid1 or x3+x5+x7==valid1:
        print('fim de jogo, player 1 venceu')
        break


    valid1 = 12


    if x1 + x2 + x3 == valid1 or x4 + x5 + x6 == valid1 or x7 + x8 + x9 == valid1 or x1 + x4 + x7 == valid1 or x2 + x5 + x8 == valid1 or x3 + x6 + x9 == valid1 or x1 + x5 + x9 == valid1 or x3 + x5 + x7 == valid1:
        print('fim de jogo')
        print('fim do jogo, player 2 venceu')
        break

    if x1!=0 and x2!=0 and x3!=0 and x4!=0 and x5!=0 and x6!=0 and x7!=0 and x8!=0 and x9!=0:
        print('VELHA, NINGUEM VENCEU!')
        break

    if n%2==0:
        q=int(input('Qual tecla o Player X deseja mexer?'))
        if q==1:
            x1=1
        if q == 2:
            x2 = 1
        if q == 3:
            x3 = 1
        if q == 4:
            x4 = 1
        if q == 5:
            x5 = 1
        if q == 6:
            x6 = 1
        if q==7:
            x7=1
        if q == 8:
            x8 = 1
        if q == 9:
            x9 = 1

    else:

        """q = int(input('Qual tecla o Player O deseja mexer?'))"""
        #VAMOS MONTAR A INTELINGENCIA POR TRAS
        l3 = [x7, x8, x9]
        l2 = [x4, x5, x6]
        l1 = [x1, x2, x3]
        print('*-*'*30)


        if sum(l1)==2:
            randoml=1
        if sum(l2)==2:
            randoml=2
        if sum(l3)==2:
            randoml=3

        if randoml==1:
            if 0 in l1:
                q=l1.index(0)+1
        elif randoml == 2:
            if 0 in l2:
                q=l2.index(0)+4
        elif randoml == 3:
            if 0 in l3:
                q=l3.index(0)+7







        if q == 1:
            x1 = 4
        if q == 2:
            x2 = 4
        if q == 3:
            x3 = 4
        if q == 4:
            x4 = 4
        if q == 5:
            x5 = 4
        if q == 6:
            x6 = 4
        if q == 7:
            x7 = 4
        if q == 8:
            x8 = 4
        if q == 9:
            x9 = 4
        randoml = r.randint(1, 3)
    n=n+1