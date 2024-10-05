#binary search
left=0
right=len(search)-1
index=-1
goal=3

while left<=right:
    mid=(left+right)//2
    if search[mid] == goal:
        index=mid
        break
    elif search[mid]>goal:
        right=mid-1
    else:
        left=mid+1

print(index)
