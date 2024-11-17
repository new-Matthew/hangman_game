from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
size_chosen_word = len(chosen_word)

print(chosen_word)
guess = input("Escolha uma letra: ").lower()

placeholder = ""

for position in  range(size_chosen_word):
    placeholder += "_ "

print(placeholder)

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter + " "
    else:
        display += "_ "

print(display)



