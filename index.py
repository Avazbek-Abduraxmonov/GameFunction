from random import choice

score = 0

while True:
    emojis = ['✌️', '👊', '🖐️']
    randomAnswer = choice(emojis)
    try:
        userMessage = input("Choose your weapon 🖐️ 👊 ✌️ (or 'stop' to end): ")
        if userMessage.lower() == 'stop':
            print(f"Your final score is: {score}")
            break
        if userMessage not in emojis:
            print("Invalid input. Please choose from 🖐️ 👊 ✌️.")
            continue

        print(f"You chose: {userMessage}")
        print(f"The computer chose: {randomAnswer}")

        if userMessage == randomAnswer:
            score += 1
            print(f"Correct! Your score is now: {score}")
        else:
            print("Incorrect! Try again.")

    except KeyboardInterrupt:
        print('\nGoodbye!')
        break
