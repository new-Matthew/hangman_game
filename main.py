from hangman_words import word_list
from hangman_arts import stages
import random

chosen_word = random.choice(word_list)
size_chosen_word = len(chosen_word)
lives = 6
placeholder = ""

for position in range(size_chosen_word):
    placeholder += "_ "

print(placeholder)

correct_guesses = []
game_over = False

while not game_over:

    display = ""
    guess = input("Escolha uma letra: ").lower()

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)


        elif letter in correct_guesses:
            display += letter   

        else:
            display += "_"
    
    if guess not in chosen_word:
        lives -= 1

    print(lives)
    print(stages[lives])
    print(display)

    if lives == 0:
        print("Você perdeu!")
        game_over = True

    if display == chosen_word:
        game_over = True
        print("você venceu!!")
 

