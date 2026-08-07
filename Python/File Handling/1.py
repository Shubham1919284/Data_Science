p=open("Python\\File Handling\\2.txt","r")

p=open("Python\\File Handling\\2.txt","w")

p.write("This is a test file.")

p.close()

p=open("Python\\File Handling\\2.txt","a")
p.write("\nThis is a new line.")

print(p.read())

p.close()
