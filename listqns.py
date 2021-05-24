

""""a python program to sort a number in ascending order using concept of bubble sort"""

mylst=[9,3,0,1,8,4,2]
for i in range(len(mylst)-1,0,-1):
    for j in range(i):
        if mylst[j] > mylst[j+1]:
            mylst[j], mylst[j+1]=mylst[j+1],mylst[j]
print(mylst)












