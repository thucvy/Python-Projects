import random
import hangman_art
import hangman_words

print(hangman_art.logo)

word = random.choice(hangman_words.word_list).upper()

display = []
game_over = False
lives = 6

for position in range(len(word)):
    display += "_"

result = "".join(display)
print(f"The word you need to guess is {result}")

while game_over is False:
    guess = input("Guess a letter: ").upper()
    if guess in display:
        print(f"You have already guessed letter {guess}. Please choose another letter to continue")
    elif guess in word:
        for position in range(len(word)):
            if guess == word[position]:
                display[position] = guess
            result = "".join(display)   
        print(f"Your guess is correct. The word is {result}. Please continue guessing until you win. You now have {lives} lives left")
    else:
        lives -= 1
        print(f"Letter {guess} is not in the word. You lose a life. Please continue guessing. You now have {lives} lives left")

    print(hangman_art.stages[6-lives])
        
        
    if "_" not in display:
        print("You've guessed the entire word right! Congratulations, you win!")
        game_over = True
    if lives == 0:
        print("You've lost all your lives. Game over!")
        game_over = True

print(f"The correct word is {word}")
