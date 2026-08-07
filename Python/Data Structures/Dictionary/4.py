l=[1,1,2,3,2,4,6,3,4,3,2,5,1,7,6,3,5,4,6,3,9,7,8,9,7,6,5,4,3,2,1]
d={}

count=0
for i in l:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1

print(f"Count of all elements in the list is: {d}")