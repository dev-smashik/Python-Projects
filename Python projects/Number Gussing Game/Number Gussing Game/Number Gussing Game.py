import random

RandomNumber = random.randrange(1, 100)

UserInput = int(input("Guess the number: "))

if UserInput > RandomNumber:
    print("Number is too high")
    print(f"Random Number is: {RandomNumber}")
elif UserInput < RandomNumber:
    print("Number is too Low")
    print(f"Random Number is: {RandomNumber}")
else:
    print("Conratulation!! you guess the correct number!!")
    print(f"Random Number is: {RandomNumber}")
