name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You're standing at the end of a dirt road. You can go left, right, or straight into the forest. Which way do you want to go? ").lower()

if answer == "left":
    answer = input("You go left and see a river. Do you want to 'swim' across or look for a 'bridge'? ").lower()

    if answer == "swim":
        print("You tried swimming, but the current is too strong, and you got swept away. You lose!")
    elif answer == "bridge":
        answer = input("You find a weak-looking bridge. Do you 'run' across or 'walk' carefully? ").lower()
        if answer == "run":
            print("You run fast, but the bridge breaks and you fall into the river. You lose!")
        elif answer == "walk":
            print("You walk slowly and make it safely across the bridge. You continue your journey!")
        else:
            print("Invalid choice. You lose.")
    else:
        print("Invalid choice. You lose.")

elif answer == "right":
    answer = input("You go right and find a dark cave. Do you want to 'enter' or 'turn back'? ").lower()

    if answer == "enter":
        answer = input("Inside, you see a treasure chest guarded by a sleeping dragon. Do you try to 'sneak' past or 'fight' the dragon? ").lower()
        if answer == "sneak":
            print("You sneak past the dragon and take the treasure. You win!")
        elif answer == "fight":
            print("You try to fight, but the dragon wakes up and defeats you. You lose!")
        else:
            print("Invalid choice. You lose.")
    elif answer == "turn back":
        print("You turn back and find a safe path leading to a sunny meadow. You rest and enjoy the view. Well done!")
    else:
        print("Invalid choice. You lose.")

elif answer == "straight":
    answer = input("You walk into the dark forest. You hear water on your left and birds on your right. Do you go 'left' or 'right'? ").lower()

    if answer == "left":
        print("You follow the water sound and find a beautiful waterfall with hidden treasure behind it. You win!")
    elif answer == "right":
        print("You follow the birds but get chased by large, angry birds and have to run back. You lose!")
    else:
        print("Invalid choice. You lose.")

else:
    print("Invalid choice. You lose.")
