from hangman_words import word_list
from hangman_arts import stages
from hangman_arts import logo
import random

print(logo)
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

    if guess in correct_guesses:
        print(f"A letra {guess} já foi escolhida")

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

    print(f"************************RESTAM {lives} VIDAS!************************")
    print(display)
    print(stages[lives])

    if lives == 0:
        print("************************Que pena, Você perdeu!************************")
        print(f"A palavra era: {chosen_word}")
        game_over = True

    if display == chosen_word:
        game_over = True
        print("************************PARABÉNS VOCÊ VENCEU!!************************")
 