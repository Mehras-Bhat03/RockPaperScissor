import random
options = ('ROCK', 'PAPER', 'SCISSOR')
running = True

while running:

    player = None
    computer = random.choice(options)



    while player not in options:
        player = input("Enter a choice (ROCK/PAPER/SCISSORS): ").upper()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("You have a TIE!")
    elif player == "ROCK" and computer == "SCISSOR":
        print("You win!")
    elif player == "PAPER" and computer == "ROCK":
        print("You win!")
    elif player == "SCISSOR" and computer == "PAPER":
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Play Again? (y/n)").lower()
    if not play_again == "y":
        running = False
print("Thanks for playing")



