word = "Ashik"
chances = 5
Guess = []
done = False

while not done:
    for letter in word:
        if letter.lower() in Guess:
            print(letter, end=" ")
        else:
            print("_", end="")


    MyGuess = input(f"Enter your text {chances}, Guss the letter: ")
    Guess.append(MyGuess.lower())
    if MyGuess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in Guess:
            done = False


if done:
    print(f"Yes, you have won the game. The word is: {word}")