import random
import hangman_words
import hangman_art

# Hangman Shapes imported from hangman_art.py file
stages = hangman_art.stages

# Word List imported from hangman_words.py file
word_list = hangman_words.word_list

# Hangman Logo imported from hangman_art.py file
print(hangman_art.logo)

choose_word = random.choice(word_list)
# Testing
#print(f'Choosen word in {choose_word}')

# Some Hint 
print(f"HINT :\n No. of letters are {len(choose_word)} and 1st letter is {choose_word[0]}\n")

list_of_words = []
for _ in range(len(choose_word)):
    list_of_words += "_"

lives = 6
end_of_game = False
while not end_of_game:
    guess = input('Choose a letter \n').lower()

    if guess in list_of_words:
        print(f"You've already guessed {guess}, Try another letter :)\n")

    for position in range(len(choose_word)):
        letter = choose_word[position]
        if (letter == guess):
            list_of_words[position] = letter

    if guess not in choose_word:
        print(f'{guess} is not in the choosen word, You loose a life :(:(')
        lives -= 1
        print(f"Life Remaining: {lives}")
        if lives == 0:
            end_of_game = True
            print("you loose :(")

    print(f"{' '.join(list_of_words)}")

    if '_' not in list_of_words:
        end_of_game = True
        print("You Win :)")

    print(stages[lives])

