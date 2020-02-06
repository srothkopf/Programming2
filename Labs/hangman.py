# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again

import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O - Help!!
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O - Oh no!!
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O - Last chance...
     /|\  |
     / \  |
          |
    =========
    '''
    ]
end_gallows = [
    '''
      +---+
          |
          |
      O  - Phew, I'm safe!
     /|\  |
     / \  |  
    =========
    ''',
    '''
      +---+
      |   |
      O - Haha, loser! Oh wait...
     /|\  |
     / \  |
          |
    =========
     +---+
      |   |
      O - Uh oh.
     /|\  |
     / \  |
          |
    =========
    '''
]

word_list = ["PYTHON","PYCHARM","GITHUB","CODING","COMPUTER","PYGAME"]
secret_word = word_list.pop(random.randrange(len(word_list) - 1))

abcs = [chr(x) for x in range(65, 65 + 26)]                            # alphabet

done = False
print("WELCOME TO HANGMAN! \nGuess my word correctly in time, or let a tiny digital man meet his fate at the end of a rope.")
wrong_guesses = []
right_guesses = []
fails = 0

while not done:
    print(gallows[fails])
    for letter in secret_word:                                         # display
        if letter in right_guesses:
            print(letter, end= " ")
        else:
            print("_ ",end= "")
    player_guess = input("\n\nMy guess is:").upper()

    if player_guess in wrong_guesses or player_guess in right_guesses: # sorting player input
        print("You already guessed that letter!")
    elif player_guess in abcs and player_guess not in secret_word:
        wrong_guesses.append(player_guess)
        print("Whoops, that's not in my word.")
        fails += 1
    elif player_guess in abcs and player_guess in secret_word:
        right_guesses.append(player_guess)
        print("Yay, you correctly guessed a letter!")
    else:
        print("Hey, that's not a letter!")

    if fails >= 7:                                                      # you lose
        print("Oh no, looks like you couldn't figure it out in time!")
        print(end_gallows[1])
        done = True
    if len(right_guesses) == len(secret_word):                          # you win
        print("You guessed my word! Congratulations!")
        print(end_gallows[0])
        done = True
    print("Incorrect guesses:", wrong_guesses)
    if done is True:                                                    # ask to play again
        again = input("Do you want to play again with a different word?").upper()
        if again == "YES" or again == "Y":
            print(
                "WELCOME AGAIN TO HANGMAN! \nGuess my word correctly in time, or let a tiny digital man meet his fate at the end of a rope.")
            wrong_guesses = []
            right_guesses = []
            fails = 0
            secret_word = word_list.pop(random.randrange(len(word_list) - 1))
            done = False
        else:
            print("Ok.")

