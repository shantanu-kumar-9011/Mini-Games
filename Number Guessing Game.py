import random

print("Welcome to the number guessing game")

top_limit = int(input("Choose a number. A random number will be chosen between zero and ur chosen number. Minimum and maximum number you can choose are 5 and 10 respectively\nYour number: "))

if top_limit < 5:
    top_limit = 5
elif top_limit >10:
    top_limit = 10


random_number = random.randint(0,top_limit)

guess = int(input("Whats your guess? "))
while True:
    if guess == random_number:
        print("Congrats!!! You won!!!")
        break
    
    elif guess > random_number:
        print("Your guess is greater than the number")
        guess = int(input("Try again: "))
    
    elif guess < random_number:
        print("Your guess is lesser than the number")
        guess = int(input("Try again: "))
print("Hope you enjoyed!!")