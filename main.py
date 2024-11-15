from getpass import getpass as input

print("EPIC 🪨📄✂️ BATTLE")
counter_1 = 0
counter_2 = 0
while True:
    print("\nSelect your move: S (scissors), P (paper), or R (rock)")

    player1 = input("Choice of player 1: ").lower()  #
    player2 = input("Choice of player 2: ").lower()  #

    if player1 == "s" and player2 == "p":
        print("1st player's Scissors has cut the 2nd player's Paper. Player 1 wins. Congrats!")
        counter_1 += 1
        print(f"{counter_1}, {counter_2}")
    elif player1 == "p" and player2 == "s":
        print("2nd player's Scissors has cut the 1st player's Paper. Player 2 wins. Congrats!")
        counter_2 += 1
        print(f"{counter_1}, {counter_2}")
    elif player1 == "p" and player2 == "r":
        print("2nd player's Rock is covered by 1st player's Paper. Player 1 wins. Congrats!")
        counter_1 += 1

    elif player1 == "r" and player2 == "p":
        print("2nd player's Paper has covered the 1st player's Rock. Player 2 wins. Congrats!")
        counter_2 += 1

    elif player1 == "s" and player2 == "r":
        print("1st player's Scissors broken from 2nd player's Rock. Player 2 wins. Play again!")
        counter_2 += 1

    elif player1 == "r" and player2 == "s":
        print("2nd player's Scissors broken from 1st player's Rock. Player 1 wins. Play again!")
        counter_1 += 1

    elif player1 == player2:
        print("It is a tie!")
    else:
        print("Invalid input! Please choose S, P, or R.")
    if counter_1 == 3 or counter_2 == 3:
        if counter_1 > counter_2:
            print(f"Player 1 wins the game! Score: {counter_1}:{counter_2}")
        else:
            print(f"Player 2 wins the game! Score: {counter_2}:{counter_1}")
        print()
        print("Thanks for playing!")
        exit()