import art, random

player_cards = []
opponent_cards = []
player_score = 0
opponent_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
check = True
check2 = True

def player_card_generator(cardslist):
    random_number = random.choice(cardslist)
    player_cards.append(random_number)
    return random_number

def opponent_card_generator(cardslist):
    random_number = random.choice(cardslist)
    opponent_cards.append(random_number)
    return random_number

def showing_hands (player, opponent, score):
    print(f"Your cards: {player}, current score: {score}")
    print(f"Computer's first card: {opponent}")

def showing_hands2 (player, opponent, score, op_score):
    print(f"Your cards: {player}, current score: {score}")
    print(f"Computer's hand: {opponent}, opponent's score: {op_score}")

def checking_scores(opponent, player):
    if player == 21:
        print("You have Blackjack, you win!")
    elif player > opponent and player < 21:
        print("You have a better score. You win!")
    elif opponent > player and opponent < 21:
        print("Your opponent has a better score. You lose.")
    elif player == opponent:
        print("Draw xD")
    elif player > 21:
        print("You lose.")
    elif opponent == 21:
        print("Your opponent did blackjack, you lose.")
    elif opponent > 21:
        print("Your opponent went over. You win!")


while check:

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

    if play == "n":
        check = False
    elif play == "y":
        check2 = True

    while check2:
        print(art.logo)
        player_cards = []
        opponent_cards = []
        player_score = 0
        opponent_score = 0

        while len(player_cards) < 2:
            player_card_generator(cards)

        opponent_card_generator(cards)
        player_score = int(sum(player_cards))
        showing_hands(player_cards, opponent_cards, player_score)

        if player_score == 21:
            checking_scores(opponent_score, player_score)

        elif player_score > 21:
            checking_scores(opponent_score, player_score)

        elif player_score < 21:
            play_2= input("Type 'y' to get another card, type 'n' to pass:").lower()
            if play_2 == "n":
                while opponent_score < player_score:
                    opponent_card_generator(cards)
                    opponent_score = int(sum(opponent_cards))
                showing_hands2(player_cards, opponent_cards, player_score, opponent_score)
                checking_scores(opponent_score, player_score)
                check2 = False

            while play_2 == "y" and check2:
                player_card_generator(cards)
                player_score = int(sum(player_cards))
                showing_hands(player_cards, opponent_cards, player_score)

                if player_score > 21:
                    checking_scores(opponent_score, player_score)
                    check2 = False

                elif player_score == 21:
                    checking_scores(opponent_score, player_score)
                    check2 = False

                elif player_score < 21:
                    play_2 = input("Type 'y' to get another card, type 'n' to pass:").lower()

                    if play_2 == "n":
                        while opponent_score < player_score:
                            opponent_card_generator(cards)
                            opponent_score = int(sum(opponent_cards))
                        showing_hands2(player_cards, opponent_cards, player_score, opponent_score)
                        checking_scores(opponent_score, player_score)
                        check2 = False


