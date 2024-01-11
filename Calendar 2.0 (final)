space=7
def print_week_day():
    day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in range(len(day)):
        print(f'{day[i]}     ',end='')
    print()

def print_day_big():
    global space
    days=[]
    for j in range(31+space):
        if j<space:
            days.append(' ')
        else:
            days.append(j-space+1)
    for i in range(len(days)):
        if i<(10+space-1) :
            print(f'{days[i]}       ',end='')
        else:
            print(f'{days[i]}      ',end='')
        if i%7==0 :
            print()
    space=int(len(days)%7)
    if space==0:
        space=7

def print_day_small():
    global space
    days=[]
    for j in range(30+space):
        if j<space:
            days.append(' ')
        else:
            days.append(j-space+1)
    for i in range(len(days)):
        if i<(10+space-1) :
            print(f'{days[i]}       ',end='')
        else:
            print(f'{days[i]}      ',end='')
        if i%7==0 :
            print()
    space=int(len(days)%7)
    if space==0:
        space=7

def print_day_February():
    global space
    days=[]
    for j in range(28+space):
        if j<space:
            days.append(' ')
        else:
            days.append(j-space+1)
    for i in range(len(days)):
        if i<(10+space-1) :
            print(f'{days[i]}       ',end='')
        else:
            print(f'{days[i]}      ',end='')
        if i%7==0 :
            print()
    space=int(len(days)%7)
    if space==0:
        space=7

def print_year():
    month=['January','February','March','April','May','June','July','August','September','October','November','December']
    big=[0,2,4,6,7,9,11]
    small=[3,5,8,10]
    for i in range(12):
        print(month[i])
        print_week_day()
        if i==1:
            print_day_February()
        for j in big:
            if i==j:
                print_day_big()
        for j in small:
            if i==j:
                print_day_small()
        print('\n')
print('Calendar for 2023')
print_year()
