import random
count=0
while(count<100):
    roll=input("press 'r' to roll a dice")
    if roll=='r':
        r=random.randint(1,6)
        print("your random no is",r)
        print("you are in position",count)
        count=count+r
        if count>100:
            print ('your number is greater than 100')
            count=count-r
        elif count==100:
            print('you win')
            break
    if count==8:
        count=37
        print('you are on')
        #here climbing the ladder.
    elif count==11:
        count=2
        print('opps')
        #here the pawn falls down.
    elif count==13:
        count=34
        print('woow amazing')
        #here the climb
    elif count==25:
        count=4
        print('no way')
        #ah going down here
    elif count==38:
        count=9
        print('ooooopps')
        #going down.
    elif count==45:
        count=68
        print('pls climb to 68')
        #climb climb climb.....
    elif count==52:
        count=81
        print('up up up...')
        #climbing here
    elif count==65:
        count==46
        print("oh no not again")
        #falls
    elif count==76:
        count=97
        print(' on and on and on')
        #up up up..
    elif count==89:
        count=70
        print("go back to 70")
        #back again.
    elif count==93:
        count=64
        print('so close')
        #down down.
    elif count<100:
        print('continue playing')
