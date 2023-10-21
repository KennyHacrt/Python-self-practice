GOOD_MESSAGE=['Try again!You can do it!!','Come on!You almost did it!','You nearly made it mate!']
def Game_mode(a,b,tries,CHANCE,recognise_level):
    PICKED_NUMBER=random.randint(a,b)
    for i in range(tries):   
        USERS_GUESS=int(input('what is your guess :  '))
        if USERS_GUESS==PICKED_NUMBER:
            print('you win!!')
            break
        elif USERS_GUESS>PICKED_NUMBER:
            CHANCE-=1
            if CHANCE==0:
                print(f'you lose!!The answer is {PICKED_NUMBER}')
                break
            if recognise_level!=0:
                print('Lower')
            print(random.choice(GOOD_MESSAGE))
            print(f'you still have {CHANCE} chances left')
        elif USERS_GUESS<PICKED_NUMBER:
            CHANCE-=1
            if CHANCE==0:
                print(f'you lose!!The answer is {PICKED_NUMBER}')
                break
            if recognise_level!=0:
                print('Higher')
            print(random.choice(GOOD_MESSAGE))
            print(f'you still have {CHANCE} chances left')
        
def number_guessing(DIFFICULT_LEVEL):
    if DIFFICULT_LEVEL=='Easy':
        Game_mode(0,10,3,3,1)
    if DIFFICULT_LEVEL=='Medium':
        Game_mode(0,100,3,3,1)
    if DIFFICULT_LEVEL=='Hard':
        Game_mode(-100,100,2,2,1)
    if DIFFICULT_LEVEL=='Insane':
        Game_mode(0,100,3,3,0)
number_guessing(input('Please choose game mode:\nEasy(Range0-10,Max 3 tries)\nMedium(Range0-100,Max 3 tries)\nHard(Range [-100] - [100],Max 3 tries)\nInsane(Range0-100,Max 3 tries,No hints)\n'))
