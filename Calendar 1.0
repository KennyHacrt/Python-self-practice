space=6
def make_space():
    space_list=[]
    for i in range(space):
        space_list.append(' ')
    return list

def print_week_day():
    day=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in range(len(day)):
        print(f'{day[i]}     ',end='')
    print()

def print_day_big():
    for i in range(1,32):
        if i<10 :
            print(f'{i}       ',end='')
        else:
            print(f'{i}      ',end='')
        if i%7==0 :
            print()
    
def print_day_small():
    for i in range(1,31):
        if i<10 :
            print(f'{i}       ',end='')
        else:
            print(f'{i}      ',end='')
        if i%7==0 :
            print()

def print_day_February():
    for i in range(1,29):
        if i<10 :
            print(f'{i}       ',end='')
        else:
            print(f'{i}      ',end='')
        if i%7==0 :
            print()

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
