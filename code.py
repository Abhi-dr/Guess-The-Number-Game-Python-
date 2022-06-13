''' ============================================ INSTRUCTIONS =====================================================

1. Welcome to our Game... Enhance your guessing power in this game.. Enjoy!...
2. You have to enter a number to which tha range will be decided...
3. For instance, if you enter 10, The range will be 0 - 10...
4. Its a 2 Player game...
5. Every Player will get 10 chances to guess the right number...
6. Winner will be decided on the basis of chances you took to guess the right number...
7. Right number will be different for both the Players
8. Eg. If Player-1 took 3 chances and Player-2 took 5 chance to guess the number, The winner will be Player-1...

                                            * ALL THE BEST *

'''

import random as rd

while True:
    a = int(input("Enter the range of numbers:- "))
    rng = rd.randint(0, a)
    line = "_" * 75

    player1 = str(input("Enter the name Player 1:- "))
    chances1 = chances2 = 9
    score1 = score2 = 10

    print(f"Hello {player1.title()}... You have {chances1 + 1} chances to guess the number... Good Luck!")
    while chances1 >= 1:
        num = int(input(f"Enter your no.:- "))

        if num == rng and num <= a:
            print(f">>> Yoo {player1}!!... You Guessed the right number... ")
            break

        elif num != rng and num <= a and num > rng:
            print(f">>> Ohh hoo... This is not the number... Try a Smaller number... Now {chances1} Chances Left...")
            chances1 -= 1
            score1 -= 1
            continue

        elif num != rng and num <= a and num < rng:
            print(f">>> Ohh hoo... This is not the number... Try a Bigger number... Now {chances1} Chances Left...")
            chances1 -= 1
            score1 -= 1
            continue

        else:
            print(">>> INVALID!!!... You Number might be OUT OF RANGE... Try Again")

    print(line)

    print(" \n\t\t\t\t\t\t Now the Number is changed for Player 2 \n ")

    rng2 = rd.randint(0, a)

    player2 = str(input("Enter your name Player 2:- "))
    print(f"Hello {player2.title()}... You also have {chances2 + 1} Chances... All The Best..")

    while chances2 >= 1:
        num2 = int(input("Enter the number:- "))

        if num2 == rng2 and num2 <= a:
            print(f">>> Yoo {player2}!!... You Guessed the right number...")
            break

        elif num2 != rng2 and num2 <= a and num2 > rng2:
            print(f">>> Ohh hoo... This is not the number... Try a Smaller Number... Now {chances2} Chances Left...")
            chances2 -= 1
            score2 -= 1
            continue

        elif num2 != rng2 and num2 <= a and num2 < rng2:
            print(f">>> Ohh hoo... This is not the number... Try a Bigger Number... Now {chances2} Chances Left...")
            chances2 -= 1
            score2 -= 1
            continue

        else:
            print(">>> INVALID!!!... You Number might be OUT OF RANGE... Try Again")

    if score1 > score2:
        print(f"\n\n\n\t\t\t\t** The Winner is {player1.capitalize()} **")
        print(line)
    elif score2 > score1:
        print(f"\n\n\n\t\t\t\t** The Winner is {player2.capitalize()} **")
        print(line)

    else:
        print("\n\n\n\t\t\t\t** Its a Draw **")
        print(line)