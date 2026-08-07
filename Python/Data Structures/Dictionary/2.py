d1={10:11,34:45,67:89,90:12}
d2={56:78,960:12,34:445,67:819}

# d1.update(d2)
# print(d1)

for key in d2:
    d1[key]=d2[key]

print(d1)
print(d2)