print("helloq")
print(5+9)
a=9/8
a=5-98
print(a)
b<-47+55
c="Shubham kumar Jha"
print(c)
my_function = function(a, b = 10) {
  return(a + b)
}

# Correct use with <- for assignment
x <- 5
result = my_function(x)  # This works fine
print(result)  # Output: 15

# Using = might cause confusion if not used carefully
x = 5  # Assigns value to x
result = my_function(x)  # Here, it's clear x is an argument
print(result)
result=my_function(98)
print(result)
# This is ambiguous and could lead to errors
data <- c(1, 2, 3)
mean(data = data)  # This might not behave as expected
