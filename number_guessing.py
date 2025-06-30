import random

print("Welcome to our Number Guessing Game : ")

low=int(input("Enter Lower Boundary: "))
High=int(input("Enter Higher Boundary: "))


num=random.randint(low,High)

ch=3 # Total allowed chances
gc=0 # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')




      