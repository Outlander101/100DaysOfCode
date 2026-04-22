import pandas
import os

# Depends on nato_phonetic_alphabet.csv file.

PHONETIC_CSV = "./nato_phonetic_alphabet.csv"
EXIT_KEY = "EXIT"

def main():
    # Additional check to validate path/file.
    if os.path.isfile(PHONETIC_CSV):
        phonetic_dict = {row.letter:row.code for (index, row) in pandas.read_csv(PHONETIC_CSV).iterrows()}

        while True:
            user_phonetic_word = input("Enter the word: ").upper()

            if user_phonetic_word == EXIT_KEY:
                break

            phonetic_list = [phonetic_dict[letter] for letter in user_phonetic_word]
            print(phonetic_list)
    else:
        print(f"Invalid file path: {PHONETIC_CSV}")

if __name__ == "__main__":
    main()


