import random
EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

def main():
    print("Welcome to the Number Guessing Game")
    number = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty Easy (E) or Hard (H): ").lower()
    tries = 0
    if difficulty == "e":
        tries = EASY_LEVEL_TRIES
    else:
        tries = HARD_LEVEL_TRIES
    retry = True
    while retry and tries > 0:
        guess = int(input("Make a guess: "))
        
        if guess == number:
            print(f"Congratulation, You have guess the number: {number} with {tries} remaining")
            retry = False
            break
        elif guess > number:
            print("Too high")
            tries -= 1
        else:
            print("Too low")
            tries -= 1
        if tries > 0:
            print("Guess again.")
        print(f"You have {tries} attempts remaining to guess the number")

if __name__ == "__main__":
    main()