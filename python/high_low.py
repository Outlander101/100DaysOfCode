import random
import os

data_set = {
    'A': {"Country": 'A', "Followers": 10},
    'B': {"Country": 'B', "Followers": 20},
    'C': {"Country": 'C', "Followers": 30},
    'D': {"Country": "D", "Followers": 40},
    'E': {"Country": 'D', "Followers": 10},
    'F': {"Country": 'A', "Followers": 5},
    'G': {"Country": 'C', "Followers": 25},
    'H': {"Country": 'A', "Followers": 12}
}

def main():
    print("Let's play Higher Lower Game")
    retry = True
    score = 0
    other = ''
    keys = list(data_set.keys())
    choice_follow = 0
    other_follow = 0
    choice1 = random.choice(keys)
    while retry:
        choice2 = random.choice(keys)
        while choice1 == choice2:
            choice2 = random.choice(keys)
        choice = input(f"Compare {choice1}: {data_set[choice1]['Country']} and {choice2}: {data_set[choice2]['Country']}: ").upper()
        if choice not in [choice1, choice2]:
            print(f"Invalid choice: {choice}")
            break
        other_key = choice2 if choice == choice1 else choice1
        choice_follow = data_set[choice]["Followers"]
        other_follow = data_set[other_key]["Followers"]
        if choice_follow < other_follow:
            print("You lost.")
            retry = False
        else:
            score += 1
            print("Correct Answer, moving to next round")
            print(f"Score: {score}")
            choice1 = choice.upper()
            os.system("cls" if os.name == 'nt' else 'clear')
        
    print(f"{choice1} has {data_set[choice1]['Followers']}, {choice2} has {data_set[choice2]['Followers']}")
    print(f"Score is {score}")

if __name__ == "__main__":
    while input("Want to play a Higher Lower Game (Y/N): ").lower() == 'y':
       main()