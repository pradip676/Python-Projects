import random 

# Get user input and validate
top_of_range = input("Type a number for a range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate random number
random_num = random.randint(0, top_of_range)
guesses = 0

# Start guessing loop
while True:
    guesses +=1
    user_guess = input("Make a guess: ")

    # Check if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please enter a number greater than 0 next time.")
            continue

    else:
        print("Please type a number next time.")
        continue

    # Check if the guess is correct
    if user_guess == random_num:
        print("You got it!")
        break
    elif user_guess > random_num :
        print("You were above the number!")
    else:
        print("you were below the number")

print()
print("You got it in", guesses, "guesses.")