import random

num=random.randint(1, 100)
guess=0
count=0

while guess!=num:
    guess=int(input("Enter your guess between 1 and 100:"))
    count+=1
    if guess<num:
        print("Your guess is too low. Try again.")
    elif guess>num:
        print("Your guess is too high. Try again.")
print(f"Congratulations! You guessed the number {num} correctly in {count} attempts.")