# test=[9,5,6,2,3,7,8,1,0,4]
test=[9,8,7,6,5,4,3,2,1,0]
size=len(test)
for i in range(size-1):
    temp=test[i]
    index=i
    for j in range(i+1,size):
        if test[i]>test[j]:
            temp=test[j]
            index=j
    test[index]=test[i]
    test[i]=temp
print(test)

