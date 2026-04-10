import random
import string

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

num_letters = int(input("Enter the number of letters: "))
num_numbers = int(input("Enter the number of numbers: "))
num_punctuation = int(input("Enter the number of punctuation characters: "))

length = num_letters + num_numbers + num_punctuation

password = []
password.extend(random.choices(letters, k=num_letters))
password.extend(random.choices(numbers, k=num_numbers))
password.extend(random.choices(punctuation, k=num_punctuation))
random.shuffle(password)
password = ''.join(password)
print("Generated password:", password)