
import random
import time

print("Welcome! Input a range for the possible numbers. Then, input an integer value and try to guess the number.")

bot_num_range = int(input("Enter the bottom of your range here: "))

top_num_range = int(input("Enter the top of your range here: "))

#Selects a random number for the player to guess.
num = random.randint(bot_num_range, top_num_range)

player_guess = None

guess_num = 0

while player_guess != num:

    player_guess = int(input("Enter your guess here: (please enter a natural number) "))

    #Measures the number of times the player guesses.
    guess_num = guess_num + 1
    
    if player_guess == num:
        print("Congratulations, you are correct!")
        print("You guessed", guess_num, "time(s).")
        print("Thanks for playing!")
        input()
        break
    else:
        print("Sorry, your guess was incorrect. Try again.")
        while guess_num > 0 and guess_num % 5 == 0:
            cont_ans = input("Do you wish to continue? (yes or no) ")
            if (cont_ans == "yes"):
                break
            elif (cont_ans == "no"):
                print("You guessed", guess_num, "time(s).")
                print("The correct number was"+num+".")
                print("Thanks for playing!")
                input()
                break
            else:
                print("Please enter valid input.")
                continue
                
input()
