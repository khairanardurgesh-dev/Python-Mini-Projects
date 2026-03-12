random = __import__("random")
name     = input("What is your name? ")
print("Hello " + name + ", welcome to this adventure!")

answer = input("Do you want to go left or right? (left/right) ").lower()
if answer == "left":
    answer = input("You come across a river, do you want to swim across or go around? (swim/around) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by a crocodile. Game over.")
    elif answer == "around":
        print("You went around and reached your destination. You win!")
    else:
        print("Not a valid option. Game over.")
elif answer == "right":
    answer = input("You come across a bridge, do you want to cross it or go back? (cross/back) ").lower()
    if answer == "cross":
        print("You crossed the bridge and were attacked by bandits. Game over.")
    elif answer == "back":
        print("You went back and found a hidden path that leads to your destination. You win!")
    else:
        print("Not a valid option. Game over.")
        answer = input("you come across a pithole do you want to jump/go back ?) ").lower()
        if answer == "jump":
            print("You swam across and were eaten by a crocodile. Game over.")
        elif answer == "go back":
            print("You went back and found a hidden path that leads to your destination. You win!")
        else:
            print("Not a valid option. Game over.")