

from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Escolha uma letra: ").lower()

for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")

print(guess)


