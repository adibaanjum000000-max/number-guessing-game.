import random

def hint(diff):
    if diff <= 3:
        return "🔥 Very close!"
    elif diff <= 10:
        return "🙂 Close!"
    else:
        return "Far away!"

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        attempts = 10
    elif choice == "2":
        attempts = 7
    elif choice == "3":
        attempts = 5
    else:
        print("Invalid choice! Defaulting to Easy mode.")
        attempts = 10

    secret = random.randint(1, 100)
    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!")

    tries = 0

    while attempts > 0:
        guess = int(input(f"\nAttempts left {attempts}. Enter guess: "))
        tries += 1
        diff = abs(secret - guess)

        if guess < secret:
            print("Too low!")
            print("Hint:", hint(diff))

        elif guess > secret:
            print("Too high!")
            print("Hint:", hint(diff))

        else:
            print(f"\n🎉 Correct! You guessed it in {tries} attempts!")
            break

        attempts -= 1

    if attempts == 0:
        print("\n❌ Out of attempts! The number was", secret)

# Main loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye 😊")
        break
