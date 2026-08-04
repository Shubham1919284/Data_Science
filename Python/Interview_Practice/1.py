print("/\\"*5)


name="Shantanu"
print(name[2:8:-2]) #This will print empty string because the step is negative and the start index is less than the end index.

a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
print(a+b+c) #This will print [1, 2, 3, 4, 5, 6, 7, 8, 9] because the + operator concatenates the lists.
print(list(zip(a,b,c))) #This will print <zip object at 0x000001F4C8C8C8C8> because the zip function returns a zip object.