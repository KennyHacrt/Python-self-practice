#total attendance of designated students in the same course
attendance=[['Li Ming',1,1,1,0,1],['Wei',1,0,0,1,1],['Jack',1,' ',0,1,1],['Zahid',0,1,1,' ',1],['Peter',1,1,1,1,1]]
for i in range(len(attendance)):
    print(attendance[i][0])
    temp=0
    error_temp=0
    for j in range(len(attendance[i])):
        if j>0 and attendance[i][j]!=' ':
            temp+=int(attendance[i][j])
        if attendance[i][j]==' ':
            error_temp+=1

    print(f'total attendance= {temp}')
    print(f'errors= {error_temp}')

#average gpa of designated students and courses
import random
scores=[['Li Ming'],['Wei'],['Jack'],['Zahid'],['Peter']]
for i in range(5):
    for j in range(5):
        scores[i].append(random.uniform(0,4))
for i in range(5):
    print(scores[i][0])
    temp=0
    for j in range(5):
        if j>0 :
            temp+=scores[i][j]
    print(f'Average GPA= {round(temp/5,1)}')

