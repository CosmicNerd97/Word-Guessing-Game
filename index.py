import os
import random

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def wordGuessingGame() -> None:
    clear_terminal()

    words = ['rainbow', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']
    
    turns = 12
    randomWord= random.choice(words)
    guess = ['_' for i in range(len(randomWord))]
    
    while turns > 0:
        clear_terminal()  # Clear the terminal before printing each guess
        currentTurn = turns
        previousTurn = 12
        print(" ".join(guess))  # Print the current guess
        if currentTurn != previousTurn:
            print("Wrong guess. Try again")
            print(f"You have {currentTurn} guesses left.")
            previousTurn = currentTurn
        guessChar = input("Guess a character:\n")
        
        if guessChar in randomWord:
            for i in range(len(randomWord)):
                if randomWord[i] == guessChar:
                    guess[i] = guessChar
            clear_terminal()  # Clear the terminal before printing each guess
            print(" ".join(guess))
            
        else:
            turns -= 1
        
        if '_' not in guess:
            print("You win")
            break

    if turns == 0:
            clear_terminal()
            print("You lose\nThe word was:", randomWord)

wordGuessingGame()
