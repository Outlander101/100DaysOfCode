import os

PLACEHOLDER = "[name]"
LETTER_PATH = "./Input/Letters/starting_letter.docx"
INVITEES_PATH = "./Input/Names/invited_names.txt"

def readNames(path):
    if os.path.isfile(path):
        with open(path) as names:
            try:
                data = names.readlines()
                return data
            except ValueError:
                print(f"Invalid Data '{data}'")
                return  
    else:
        print(f"Invalid Path '{path}'")
        return

def create_letters(path, data):
    if os.path.isfile(LETTER_PATH):
        with open(LETTER_PATH) as letter:
            try:
                letter_content = letter.read()
                for name in data:
                    stripped_name = name.strip()
                    new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
                    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode='w') as letters:
                        letters.write(new_letter)
            except ValueError:
                print(f"Invalid content '{letter_content}'")
    else:
        print(f"Invalid Path '{path}'")
    

def main():
    names = readNames(INVITEES_PATH)
    create_letters(LETTER_PATH, names)

if __name__ == "__main__":
    main()