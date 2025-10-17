from turtle import left


print("Welcome to the tresure Game!")
print("Have have fun playing.")

choice = input("You are at crossroads, which side would like to take?\n"
               "Left or Right\n").lower()
if choice == "left":
    choice1 = input("You have come to a lake. There is an island in the middle of the lake.\n"
                    'Type "swim" to swim across or type "wait" to wait for the boat.\n').lower()
    if choice1 == "wait":
        choice2 = input("You have reached the island, very safe & unharmed.\n"
                        "There is a house with three colored doors. One is red\n"
                        "one is yellow and the other one is blue.\n"
                        "Choose one door to enter.\n").lower()
        if choice2 == "red":
            print("You have entered a room full of fire. Game Over!")
        elif choice2 == "yellow":
            print("You have found the treasure. You Win!")
        elif choice2 == "blue":
            print("You have entered a room full of beasts. Game Over!")
        else:
            print("Sorry, the door you chose doesn't  exist. Game Over!")
    else:
        print("Whooo, you just got eaten by a crocodile. Game Over!")
else:
    print("You just fell into a shit hole. Game Over!")

    