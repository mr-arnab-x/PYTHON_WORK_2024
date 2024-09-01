import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        user_guess = input("Take a guess : ")

        ##---------IF WANT TO ADD QUIT OPTION-------------------

    
        # user_guess = input("Take a guess or Quit(Q): ")
        # if user_guess == 'Q':
        #     break


        # Check if the input is a number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Your guess is too low.")
        elif user_guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    print ("---------------GAME OVER----------------")

if __name__ == "__main__":
    number_guessing_game()
