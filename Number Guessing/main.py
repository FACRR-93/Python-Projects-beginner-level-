import art, random
print(art.logo)

attempts = 0
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_generated = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
    flag = True
    while flag:
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < number_generated:
                print("Too low.")
                print("Guess again")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses. Try again")
                    flag = False
            elif guess > number_generated:
                print("Too high.")
                print("Guess again")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses. Try again")
                    flag = False
            elif guess == number_generated:
                print(f"You got it! The answer was {number_generated}")
                attempts = 0
                flag = False


elif difficulty == "hard":
    attempts = 5
    flag = True
    while flag:
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < number_generated:
                print("Too low.")
                print("Guess again")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses. Try again")
                    flag = False

            elif guess > number_generated:
                print("Too high.")
                print("Guess again")
                attempts -= 1
                if attempts == 0:
                    print("You've run out of guesses. Try again")
                    flag = False

            elif guess == number_generated:
                print(f"You got it! The answer was {number_generated}")
                attempts = 0
                flag = False
