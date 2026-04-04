import random

def get_random_word():
    words = ['python', 'hangman', 'programming', 'challenge', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, and both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso, and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head only
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial empty state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play_hangman():
   word = get_random_word()
   word_completed = '_' * len(word)
   guessed = False
   guessed_letter = []
   guessed_word = []
   tries = 6
   print("Lets play Hangman!")
   print(display_hangman(tries))
   print(word_completed)
   print("\n")
   while not guessed and tries > 0:
      guess = input("Please guess a letter or word: ").lower()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letter:
            print("You already guessed the letter ", guess)
         elif guess not in word:
            print(guess , " is not in the word.")
            tries -= 1
            guessed_letter.append(guess)
         else:
            print("Good Job ", guess,  " is in the word!")
            guessed_letter.append(guess)
            word_completed_list = list(word_completed)
            indices = [i for i, letter in enumerate(word) if letter == guess]   
            for index in indices:
               word_completed_list[index] = guess
            word_completed = ''.join(word_completed_list)
            if '_' not in word_completed:
               guessed = True
      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_word:
            print("You already guessed the word ", word)
         elif guess != word:
            print(guess, " is not the word.")
            tries -= 1
            guessed_word.append(guess)
         else:
            guessed = True
            word_completed = word
      else:
         print("Not a valid guess.")
      print(display_hangman(tries))
      print(word_completed)
      print("\n")

      if guessed:
         print("Congratulations! You guessed the word! You win!")
      else:
         print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

# def play_hangman():
#     word = get_random_word()
#     word_completion = '_' * len(word)
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     tries = 6
#     print("Let's play Hangman!")
#     print(display_hangman(tries))
#     print(word_completion)
#     print("\n")
#     while not guessed and tries > 0:
#         guess = input("Please guess a letter or word: ").lower()
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("You already guessed the letter ", guess)
#             elif guess not in word:
#                 print(guess, " is not not in the word.")
#                 tries -= 1
#                 guessed_letters.append(guess)
#             else:
#                 print("Good Job, ", guess, " is in the word!")
#                 guessed_letters.append(guess)
#                 word_completion_list = list(word_completion)
#                 indices = [i for i, letter in enumerate(word) if letter == guess]
#                 for index in indices:
#                     word_completion_list[index] = guess
#                     word_completion = ''.join(word_completion_list)
#                     if '_' not in word_completion:
#                         guessed = True
#         elif len(guess) == len(word) and guess.isalpha():
#             if guess in guessed_words:
#                 print("You already guessed the word ", guess)
#             elif guess != word:
#                 print(guess, " is not the word")
#                 tries -= 1
#                 guessed_words.append(guess)
#             else:
#                 guessed = True
#                 word_completion = word
#         else:
#             print("Not a valid guess.")
        
#         print(display_hangman(tries))
#         print(word_completion)
#         print("\n")

#     if guessed:
#         print("Congratulations! You guessed the word! You win!")
#     else:
#         print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

if __name__ == "__main__":
   play_hangman()

    # word = get_random_word()
    # word_completion = '_' * len(word)
    # guessed = False
    # guessed_letters = []
    # guessed_words = []
    # tries = 6

    # print("Let's play Hangman!")
    # print(display_hangman(tries))
    # print(word_completion)
    # print("\n")

    # while not guessed and tries > 0:
    #     guess = input("Please guess a letter or word: ").lower()
    #     if len(guess) == 1 and guess.isalpha():
    #         if guess in guessed_letters:
    #             print("You already guessed the letter", guess)
    #         elif guess not in word:
    #             print(guess, "is not in the word.")
    #             tries -= 1
    #             guessed_letters.append(guess)
    #         else:
    #             print("Good job,", guess, "is in the word!")
    #             guessed_letters.append(guess)
    #             word_as_list = list(word_completion)
    #             indices = [i for i, letter in enumerate(word) if letter == guess]
    #             for index in indices:
    #                 word_as_list[index] = guess
    #             word_completion = "".join(word_as_list)
    #             if "_" not in word_completion:
    #                 guessed = True
    #     elif len(guess) == len(word) and guess.isalpha():
    #         if guess in guessed_words:
    #             print("You already guessed the word", guess)
    #         elif guess != word:
    #             print(guess, "is not the word.")
    #             tries -= 1
    #             guessed_words.append(guess)
    #         else:
    #             guessed = True
    #             word_completion = word
    #     else:
    #         print("Not a valid guess.")

    #     print(display_hangman(tries))
    #     print(word_completion)
    #     print("\n")

    # if guessed:
    #     print("Congratulations! You guessed the word! You win!")
    # else:
    #     print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")