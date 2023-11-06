import random
#make a matrix with random dimensions and numbers inside must be 0
def matrix(row,column):
    OUTSIDE_LIST=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            temp.append(0)
        OUTSIDE_LIST.append(temp)
    return OUTSIDE_LIST
#add numbers in to matrix
def ADD_ELEMENT(TWO_D_LIST,number):
    for i in range(len(TWO_D_LIST)):
        for j in range(len(TWO_D_LIST[i])):
            TWO_D_LIST[i][j]+=number
    return TWO_D_LIST
#make matrix without brackets,only numbers 
def PURE_MATRIX(matrix_input):
    for i in range(len(matrix_input)):
        for j in range(len(matrix_input[i])):
            print(matrix_input[i][j],end='  ')
        print('\n')
#transpose matrix
def TRANSPOSE(matrix_input):
    transpose_matrix=[]
    for i in range(len(matrix_input[0])):
        temp=[]
        for j in range(len(matrix_input)):
            temp.append(matrix_input[j][i])
        transpose_matrix.append(temp)
    return transpose_matrix
#make a random matrix
def random_matrix(row,column):
    OUTSIDE_LIST=[]
    for i in range(row):
        temp=[]
        for j in range(column):
            temp.append(random.randint(0,9))
        OUTSIDE_LIST.append(temp)
    return OUTSIDE_LIST
#enter two matrix and multiply
def multiply_function(matrix_1,matrix_2):
    new_matrix=[]
    for out in range(3):
        temp=[]
        for j in range(3):
            a=0
            for k in range(3):
                a+=matrix_1[out][k]*matrix_2[k][j]
            temp.append(a)
        new_matrix.append(temp)
    return new_matrix
