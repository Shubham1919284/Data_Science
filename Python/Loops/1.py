n=int(input("Enter a number: "))

# for i in range(n):
#     print("hello world")

# -----------------------------------------------------------------------------------------------------------------------------
# for i in range(1,n+1):
#     print(i)

# -----------------------------------------------------------------------------------------------------------------------------
# for i in range(n,0,-1):
#     print(i)

# -----------------------------------------------------------------------------------------------------------------------------
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# -----------------------------------------------------------------------------------------------------------------------------
# x=0
# for i in range(1,n+1):
#     x+=i
# print(x)

# -----------------------------------------------------------------------------------------------------------------------------
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print(fac)

# -----------------------------------------------------------------------------------------------------------------------------
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Sum of even numbers from 1 to {n} is: {even}")
# print(f"Sum of odd numbers from 1 to {n} is: {odd}")

# -----------------------------------------------------------------------------------------------------------------------------
# factors=[]
# for i in range(1,n+1):
#     if n%i==0:
#         factors.append(i)
# print(f"Factors of {n} are: {factors}")

# -----------------------------------------------------------------------------------------------------------------------------
# factors=[]
# pn=0
# for i in range(1,n):
#     if n%i==0:
#         factors.append(i)
#         pn+=i
# print(f"Factors of {n} are: {factors}")
# print(f"Sum of factors of {n} is: {pn}")
# if pn==n:
#     print(f"{n} is a perfect number.")  
# else:
#     print(f"{n} is not a perfect number.")

# -----------------------------------------------------------------------------------------------------------------------------
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

# -----------------------------------------------------------------------------------------------------------------------------
# a="Shubham"
# temp=""
# for i in range(len(a),0,-1):
#     temp+=a[i-1]
# l=reversed(a)
# print(l)
# print(f"Reverse of {a} is: {temp}")
# if a==temp:
#     print(f"{a} is a palindrome.")
# else:
#     print(f"{a} is not a palindrome.")    

# -----------------------------------------------------------------------------------------------------------------------------
a="SHua1239@#$48sdj"

digit=0
char=0
spchar=0
for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1

print(f"Number of digits in {a} is: {digit}")
print(f"Number of characters in {a} is: {char}")
print(f"Number of special characters in {a} is: {spchar}")
