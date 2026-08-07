d1={10:100,20:200,30:300,40:400}
d2={10:500,40:600,70:700,80:800}

print("Dictionary d1:")
print(d1)

print("Dictionary d2:")
print(d2)

for key in d2:
    if key in d1.keys():
        d1[key]+=d2[key]
    else:
        d1[key]=d2[key]

        
print("After Merging d1 and d2:")
print(d1)