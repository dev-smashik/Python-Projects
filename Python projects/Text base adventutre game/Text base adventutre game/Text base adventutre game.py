answer = input("do you want to play this game? [Yes/No]: ")

if answer == "yes":
    print("Welcome to the game!")
    answer = input("do you want to go jungle or cave? [Jungle/Cave]: ")
    if answer == "jungle":
        print("you see the hungry tiger then tiger will eat you and you lose the game")
        print("the game is now closed")
    elif answer == "cave":
        print("you see the bear in front of cave")
        answer = input("do you want to fight with the bear or run away? [fight/run]: ")
        if answer == "fight":
            print("bear is too string! you lose the game!")
            print("the game is now closed")
        elif answer == "run":
            print("you save your life from bean and you won the game!")
            print("the game is now closed")
else:
    print("the game is now closed")

