coins = 0
while True:
    print("You have " +  str(coins) + " coins")
    change = input("Do you want another?")
    if change == "yes":
        coins += 1
    elif change == "no":
        print("Bye")
        break