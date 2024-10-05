def Fibonacci_numbers(no):
    a,b=0,1
    key=1
    print(a, end = ' ')
    if no>=2:
        print(b, end = ' ') 
    if no>2:
        for i in range(no-2):
            if key==4:
                key=1
            if key==1:
                c=a+b
                print(c, end = ' ')
            elif key==2:
                a=b+c
                print(a, end = ' ')
            elif key==3:
                b=c+a
                print(b, end = ' ')
            key+=1
            


required_no=int(input('enter numbers you want,integers only   :'))
Fibonacci_numbers(required_no)



#better and shorter method, made it a function
def Fibonacci_numbers(no):
    a,b=1,1
    for i in range(no):
        if i%2==1:
            print(a,end=' ')
            a=a+b
            
        else:
            print(b,end=' ')
            b=a+b
Fibonacci_numbers(8) 



#advance code,put them all into a list and return it to the function
def Fibonacci_numbers(no):
    a,b=1,1
    MY_LIST=[]  
    for i in range(no):
        if i%2==1:
            MY_LIST.append(a)
            a=a+b
            
        else:
            MY_LIST.append(b)
            b=a+b
        if i==no-1:
            return MY_LIST

print(Fibonacci_numbers(8))    
