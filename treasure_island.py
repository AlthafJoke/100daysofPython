print("Welcome to Treasure island.")
print("Your mission is to find the treasure")

choice1 = input('You\'re at a crossroad, where do you want to go ? Type "left" or "right".').lower()
print(choice1)


if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat . Type 'swim' to swim across. ").lower()
    if choice2 == "wait":
        choice3 = input("You have reached the island unharmed. There is a house with 3 doors. One is red, one yellow and one blue. which color do you choose?").lower()
        if choice3 == "yellow":
            print("congratulation!. You have found the treasure. You Win")
        elif choice3 == "blue":
            print("you entered the room full of beasts. Game Over.")
        elif choice3 == "red":
            print("print its room full of fire . Game Over.")
        else:
            print("choice doesnot exist. Game Over.")
        
    else:
        print("You got eaten by the crocodile, Game Over.")
else:
    print("You fell into a hole , Game Over.")