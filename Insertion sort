# test=[9,5,6,2,3,7,8,1,0,4]
test=[9,8,7,6,5,4,3,2,1,0]
size=len(test)
for i in range(size-1):
    if test[i]>test[i+1]:
        for j in range(i,-1,-1):
            if test[j]<test[j+1]:
                break
            temp=test[j+1]
            test[j+1]=test[j]
            test[j]=temp
print(test)
