a=int(input("Enter a number: "))
print(f"The number for division is: {a}")

# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

try:
    print(10/a)

except Exception as err:
    print(f"Error: {err}")

else:
    print("Division successful.") #This block will execute only if no exception occurs in the try block.

finally:
    print("I will run no matter what.") #This block will always execute, regardless of whether an exception occurred or not.

raise Exception("This is a custom exception.") #This will raise a custom exception after the try-except-finally block.