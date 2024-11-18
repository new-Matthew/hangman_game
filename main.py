from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
size_chosen_word = len(chosen_word)

print(chosen_word)

placeholder = ""

for position in range(size_chosen_word):
    placeholder += "_"

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
            print(letter)

        elif letter in correct_guesses:
            display += letter   
            print(letter)
        else:
            display += "_"

    for letter in chosen_word:
        if display == chosen_word:
            game_over = True
            print("você venceu!!")
            print(letter)

    print(correct_guesses)
    print(display)

if game_over == True:
    print("Você venceu!")

