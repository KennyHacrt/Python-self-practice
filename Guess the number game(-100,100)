guess=random.randint(-100,100)
print(guess)
while True:
    ans=int(input('please pick an integer between -100 and 100  :'))
    if ans==guess:
        print('bingo')
        break
    
    diff=abs(guess-ans)
    
    per=(diff/200)*100
    
    if per<2:
        print('Your guess is very close') 
    elif per<5 and ans<guess:
        print('Your guess is a bit little lower')
    elif per<5 and ans>guess:
        print('Your guess is a bit little higher')
    
    elif per>5 and per<10 and ans>guess:   
        print('Your guess is a little higher')
    elif per>5 and per<10 and ans<guess:   
        print('Your guess is a little lower')
    
    elif per>10 and ans<guess:
        print('Your guess is  too lower')
    elif per>10 and ans>guess:
        print('Your guess is  too higher')
