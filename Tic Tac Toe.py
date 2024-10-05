import os
BOARD_lOOKS=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
times=1
def print_board_template():
    BOARD_temp=[[1,2,3],[4,5,6],[7,8,9]]
    for i in range(3):
        for j in range(3):
            print(f' {BOARD_temp[i][j]}',end='')
            if j<2:
                print(' |',end='')
        print()
        if i<2:
            print('-----------')

def print_board_current():
    for i in range(3):
        for j in range(3):
            print(f' {BOARD_lOOKS[i][j]}',end='')
            if j<2:
                print(' |',end='')
        print()
        if i<2:
            print('-----------')

def print_board(input,symbol):
    key=1
    for i in range(3):
            for j in range(3):
                if key==input:
                    BOARD_lOOKS[i][j]=symbol
                    
                key+=1
    for i in range(3):
        for j in range(3):
            print(f' {BOARD_lOOKS[i][j]}',end='')
            if j<2:
                print(' |',end='')
        print()
        if i<2:
            print('-----------')

def who_wins_system ():
    if determine_win_or_not(0,0,1,1,2,2)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,0,1,1,2,2)==False:
        return 'player 2 wins'
    if determine_win_or_not(0,0,1,0,2,0)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,0,1,0,2,0)==False:
        return 'player 2 wins'
    if determine_win_or_not(0,1,1,1,2,1)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,1,1,1,2,1)==False:
        return 'player 2 wins'
    if determine_win_or_not(0,2,1,2,2,2)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,2,1,2,2,2)==False:
        return 'player 2 wins'
    if determine_win_or_not(0,0,0,1,0,2)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,0,0,1,0,2)==False:
        return 'player 2 wins'
    if determine_win_or_not(1,0,1,1,1,2)==True:
        return 'player 1 wins'
    if determine_win_or_not(1,0,1,1,1,2)==False:
        return 'player 2 wins'
    if determine_win_or_not(2,0,2,1,2,2)==True:
        return 'player 1 wins'
    if determine_win_or_not(2,0,2,1,2,2)==False:
        return 'player 2 wins'
    if determine_win_or_not(0,2,1,1,2,0)==True:
        return 'player 1 wins'
    if determine_win_or_not(0,2,1,1,2,0)==False:
        return 'player 2 wins'
    
def determine_win_or_not(a,b,c,d,e,f):
    if BOARD_lOOKS[a][b]=='O' and BOARD_lOOKS[c][d]=='O' and BOARD_lOOKS[e][f]=='O':
        return True
    if BOARD_lOOKS[a][b]=='X' and BOARD_lOOKS[c][d]=='X' and BOARD_lOOKS[e][f]=='X':
        return False


for i in range(9):
    print_board_template()
    print_board_current()
    print('player 1 is O and player 2 is X ')
    if times%2 != 0:
        player_1=int(input('please select the location you want player 1 : '))

        print_board(player_1,'O')
    else:
        player_2=int(input('please select the location you want player 2 : '))
        print_board(player_2,'X')
    times+=1
    if who_wins_system()=='player 1 wins' or who_wins_system()=='player 2 wins':
        os.system("clear") 
        print_board_current()
        print(who_wins_system())
        break
    if i==8:
        os.system("clear") 
        print_board_current()
        print('draw')
        break
    os.system("clear") 
