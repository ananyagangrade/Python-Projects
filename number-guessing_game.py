import random
correct = random.randint(1, 10)
while True:
    try:
        num = int(input("Guess the number: "))
        if num == correct:
            print("Great!! You won the game.")

        elif num > correct:
            print("Too high!")

        elif num < correct:
            print("Too low")

        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid value.")
