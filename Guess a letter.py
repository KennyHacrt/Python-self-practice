import random
print('hello welcome to word guessing game')
WORDLIST=['python','hacker','origin','maggie','kenny']
chosen=random.choice(WORDLIST)
print(chosen)
guess=input('please enter a letter(try to guess!) :\n')
def isguess():
    for i in chosen:
        if guess.lower()==i:
            return 1
    return 0
final= isguess()
if final:
    print('Congrats! The letter is in this vocab!')
else:
    print("It's not there")



