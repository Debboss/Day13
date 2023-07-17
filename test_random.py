import random

def random_number_generator():
    global random_number
    random_number = random.randint(1, 100)

random_number_generator()

def easy_level():
    attempts = 10
    print("You have 10 attempts remaining to guess the number")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
        else:
            print("Congratulations! You guessed the number correctly!")
            return
        attempts -= 1
        print(f"{attempts} tries are remaining.")
    print("You ran out of attempts. The number was:", random_number)

def hard_level():
    attempts = 5
    print("You have 5 attempts remaining to guess the number")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
        else:
            print("Congratulations! You guessed the number correctly!")
            return
        attempts -= 1
        print(f"{attempts} tries are remaining.")
    print("You ran out of attempts. The number was:", random_number)



print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

level = input("Choose difficulty:\n'easy' or 'hard': ")

if level == "easy":
    easy_level();
else:
    hard_level();
