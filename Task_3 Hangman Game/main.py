import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)

choosen_word = random.choice(word_list)


lives = 6

len = len(choosen_word)
display = []
for letters in choosen_word:
    display += "_"
print(display)

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f'Letter {guess} has already been guessed.')
    for position in range(len):
        letters = choosen_word[position]
        if letters == guess:
            display[position] = letters
    print(display)
    
    if "_" not in display:
       game_over = True
       print("You won.")
       
    if guess not in choosen_word:
        lives -= 1
        print(f'You guessed letter {guess}, thats not in the word. You lose a live.')
        if lives == 0:
            game_over = True
            print("You loose.")
    print(stages[lives])                                
