import random
import msvcrt

def play_game():
    random_number = random.randint(0, 100)
    tries = 0   # Starting tries

    print("Welcome to my number guessing game!")

    while True:
        guess = input("Guess the number between 0 and 100: ")

        if guess.lstrip('-').isdigit():  # Check if the input is a valid number including negative numbers
            guess = int(guess)
            tries += 1  # Increment tries after each guess
            if guess == random_number:
                print("Congratulations! You've guessed the correct number!")
                print(f"Number of tries: {tries}")
                return  # End the function, allowing the user to choose whether to play again
            elif guess < random_number:
                print("The number is higher. Try again.")
            else:
                print("The number is lower. Try again.")
        else:
            print("Please enter a valid number.")

print("Welcome to my number guessing game!")
playing = input("Would you like to play? ")

while playing.lower() == "yes":
    play_game()
    playing = input("Would you like to play again? ")

print("Thank you for playing!")

print("Press any key to exit the program...")


# Wait for any key press to exit program
msvcrt.getch()
