# Project3: Pick a Card Game!
# Go Fish!!

import random
from go_fish_rules import go_fish_rules


def the_pool():
    pool = []
    alphabet = ["Ace", "Jack", "Queen", "King"]
    for deck in range(4):
        for card in range(2, 11):
            pool.append(str(card))
        for card in alphabet:
            pool.append(card)

    random.shuffle(pool)

    return pool


pool_fish = the_pool()

Read_Rules = input(str("You can type '--help' to read about Go Fish rules.\n"))
if Read_Rules == "--help":
    print(go_fish_rules)


while True:
    number_of_player = input("\nPlease select 1 or 2 player(s).\n")

    if str(number_of_player) == "--help":
        print(go_fish_rules)
        print("\nYou can type '--resume' to continue your game.")
        go_back = str(input(""))
        if go_back == "--resume":
            continue

    if int(number_of_player) == 1:
        print("\n1 Player Mode\n")

        player1_hand = list()
        player2_hand = list()
        player1_pairs = 0
        player2_pairs = 0

        for i in range(7):
            fish = pool_fish.pop()
            player1_hand.append(fish)

        print("Your fish: ", player1_hand)

        for i in range(7):
            fish = pool_fish.pop()
            player2_hand.append(fish)

        print("\n\n Let's play Go Fish! \n")


        def check_for_pairs(hand):
            point = 0

            for card in hand:
                if hand.count(card) > 1:
                    hand.remove(card)
                    hand.remove(card)
                    point += 1

            return point


        player1_pairs = check_for_pairs(player1_hand)
        player2_pairs = check_for_pairs(player2_hand)

        while True:
            if len(player1_hand) == 0:
                break
            if len(player2_hand) == 0:
                break
            if len(pool_fish) == 0:
                break
            else:
                while True:
                    print("Your current fish: ", player1_hand)
                    wanted_card = input("What card do you want? \n")
                    if wanted_card == "A":
                        wanted_card = "Ace"
                    if wanted_card == "J":
                        wanted_card = "Jack"
                    if wanted_card == "Q":
                        wanted_card = "Queen"
                    if wanted_card == "K":
                        wanted_card = "King"
                    if wanted_card == "--help":
                        print(go_fish_rules)
                        print("\nYou can type '--resume' to continue your game.")
                        go_back = str(input(""))
                        if go_back == "--resume":
                            continue

                    if wanted_card in player2_hand:
                        print("Good job!")
                        player1_hand.remove(wanted_card)
                        player2_hand.remove(wanted_card)
                        player1_pairs += 1
                        if len(player1_hand) == 0:
                            break
                        else:
                            continue
                    else:
                        print("Go Fish!")
                        player1_hand.append(pool_fish.pop())
                        print("Your current fish: ", player1_hand)
                        break
                player1_pairs += check_for_pairs(player1_hand)
                if len(player1_hand) == 0:
                    print("Your current fish: ", player1_hand)
                    break
                if len(pool_fish) == 0:
                    print("Empty pool!")
                    break

                while True:
                    card_choice = random.choice(player2_hand)
                    print("Computer asked for " + card_choice)
                    if card_choice in player1_hand:
                        player1_hand.remove(card_choice)
                        player2_hand.remove(card_choice)
                        player2_pairs += 1
                        if len(player2_hand) == 0:
                            break
                        else:
                            continue
                    else:
                        print("Computer had to go fishing.")
                        player2_hand.append(pool_fish.pop())
                        break
                player2_pairs += check_for_pairs(player2_hand)
                if len(player2_hand) == 0:
                    print("Computer current fish: ", player2_hand)
                    break
                if len(pool_fish) == 0:
                    print("Empty pool!")
                    break

        print("\n\n Game Over! \n\n" + "Scores:")
        print("You : ", player1_pairs)
        print("Computer : ", player2_pairs)

        if player1_pairs > player2_pairs:
            print("\n You Won!")
            break

        if player2_pairs > player1_pairs:
            print("\n Computer Won!")
            break

        else:
            print("")
            break

    if int(number_of_player) == 2:
        print("\n 2 Players Mode.\n")
        print("\nPlease enter your name.\n")
        player_one_name = input("Player 1: ")
        Player1 = str(player_one_name)
        player_two_name = input("Player 2: ")
        Player2 = str(player_two_name)

        print("\nHello! " + Player1 + " and " + Player2 + ".")

        player1_hand = list()
        player2_hand = list()
        player1_pairs = 0
        player2_pairs = 0

        for i in range(7):
            fish = pool_fish.pop()
            player1_hand.append(fish)

        for i in range(7):
            fish = pool_fish.pop()
            player2_hand.append(fish)

        print("\n\n Let's play Go Fish! \n")


        def check_for_pairs(hand):
            point = 0

            for card in hand:
                if hand.count(card) > 1:
                    hand.remove(card)
                    hand.remove(card)
                    point += 1

            return point


        player1_pairs = check_for_pairs(player1_hand)
        player2_pairs = check_for_pairs(player2_hand)

        player = 1

        while True:
            if player == 1:
                print("It's " + Player1 + "'s turn")
                try:
                    any_key = input("Press Enter to continue.\n")
                    valid_input = True
                finally:
                    print("\n" * 40)

                if len(player1_hand) == 0:
                    break
                if len(player2_hand) == 0:
                    break
                if len(pool_fish) == 0:
                    print("Empty pool!")
                    break
                else:
                    while True:
                        print("Your current fish: ", player1_hand)
                        wanted_card = input("What card do you want? \n")
                        if wanted_card == "A":
                            wanted_card = "Ace"
                        if wanted_card == "J":
                            wanted_card = "Jack"
                        if wanted_card == "Q":
                            wanted_card = "Queen"
                        if wanted_card == "K":
                            wanted_card = "King"
                        if wanted_card == "--help":
                            print(go_fish_rules)
                            print("\nYou can type '--resume' to continue your game.")
                            go_back = str(input(""))
                            if go_back == "--resume":
                                continue

                        if wanted_card in player2_hand:
                            print("Good job " + Player1 + "!")
                            player1_hand.remove(wanted_card)
                            player2_hand.remove(wanted_card)
                            player1_pairs += 1

                            if len(player1_hand) == 0:
                                break
                            else:
                                continue
                        else:
                            print("Go Fish!")
                            player1_hand.append(pool_fish.pop())
                            print(Player1 + " current fish: ", player1_hand)
                            break

                    player1_pairs += check_for_pairs(player1_hand)
                    if len(player1_hand) == 0:
                        print(Player1 + " current fish: ", player1_hand)
                        break
                    if len(pool_fish) == 0:
                        print("Empty pool!")
                        break
                    else:
                        print("\n" * 40)
                        player = 2

            else:
                print("It's " + Player2 + "'s turn")
                try:
                    any_key = input("Press Enter to continue.\n")
                    valid_input = True
                finally:
                    print("\n" * 40)
                while True:
                    print("Your current fish: ", player2_hand)
                    wanted_card = input("What card do you want? \n")
                    if wanted_card == "A":
                        wanted_card = "Ace"
                    if wanted_card == "J":
                        wanted_card = "Jack"
                    if wanted_card == "Q":
                        wanted_card = "Queen"
                    if wanted_card == "K":
                        wanted_card = "King"
                    if wanted_card == "--help":
                        print(go_fish_rules)
                        print("\nYou can type '--resume' to continue your game.")
                        go_back = str(input(""))
                        if go_back == "--resume":
                            continue

                    if wanted_card in player1_hand:
                        print("Good job " + Player2 + "!")
                        player1_hand.remove(wanted_card)
                        player2_hand.remove(wanted_card)
                        player2_pairs += 1

                        if len(player2_hand) == 0:
                            break
                        else:
                            continue
                    else:
                        print("Go Fish!")
                        player2_hand.append(pool_fish.pop())
                        print(Player2 + " current fish: ", player2_hand)
                        break
                player2_pairs += check_for_pairs(player2_hand)
                if len(player2_hand) == 0:
                    print(Player2 + " current fish: ", player2_hand)
                    break
                if len(pool_fish) == 0:
                    print("Empty pool!")
                    break
                else:
                    print("\n" * 40)
                    player = 1

        print("\n" * 10)
        print("Game Over! \n\n" + "Scores:")
        print(Player1 + ": ", player1_pairs)
        print(Player2 + ": ", player2_pairs)

        if player1_pairs > player2_pairs:
            print("")
            print(Player1 + " Won!")
            break

        if player2_pairs > player1_pairs:
            print("")
            print(Player2 + " Won!")
            break

        else:
            print("")
            break
