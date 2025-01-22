import random
import hangman_words
import hangman_art

lives = 3
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)


#  ----------hiding the letters for hint purpose----------
def hide_letter(word):
    letters = word[1::2]
    return '_'.join(letters)
hidden_word = hide_letter(chosen_word)
print("HINT:",f"_{hidden_word}_")
#  ----------hiding the letters for hint purpose----------


#  __________shuffling the letters and hiding letters___________
# def shuffle_word(word):
#     word_list = list(word)
#     random.shuffle(word_list)
#     shuffled_word = '_'.join(word_list)
#     return shuffled_word[::2]
# shuffled_word = shuffle_word(chosen_word)
# print("HINT:",f"_{shuffled_word}_")
#  __________shuffling the letters and hiding letters___________

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("guess the word: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"**************************** {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed the word: \"{guess}\"")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("guess the word: " + display)

    print(hangman_art.stages[lives])
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print("The word was", chosen_word)

    if "_" not in display:
        game_over = True
        print("****************************YOU WON****************************")

