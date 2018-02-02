import random
count=0
while(count<=100):
    roll=input("press 'r' to roll a dice")
    if roll=='r':
        r=random.randint(1,6)
    
    print("your random no is",r)
    print("you are in position",count)
    count=count+r
    print(count)

    if count==100:
        print('you win')

    elif count==8:
        count=37
        print('you are on')
    elif count==11:
        count=2
        print('opps')
    elif count==13:
        count=34
        print('woow amazing')
    elif count==25:
        count=4
        print('no way')
    elif count==38:
        count=9
        print('ooooopps')    
    elif count==45:
        count=68
        print('pls climb to 68')
    elif count==52:
        count=81
        print('up up up...')
    elif count==93:
        count=64
        print('so close')
