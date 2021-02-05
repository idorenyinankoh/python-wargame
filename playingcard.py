from cardclass import *
from random import*
cardDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Playing(Card):
    def __init__(self):
        Card.__init__(self, cardDeck)


newCard = Playing()
ar, br = newCard.shufflein()
# print(ar)
# print(br)

# playerOne = newCard.deckone(ar)
# print(playerOne)
# playerTwo = newCard.decktwo(br)
# print(playerTwo)
holding = []

while True:
    card = input('continue playing by typing Yes or Exit by typing No ')
    card = card.strip().lower()

    if card == 'no':
        print('Thank you. hope to see you again. Bye')  
        break
    # print(f"present length of player two  {len(br)}")
    if card != 'yes':
        print('Invalid input.')
        continue
    else:
        # print(f"user input is {card}")
        # print('start')
        # print(ar)
        # print(br)
        # print('----------poppin cards------------')
        playerOne = newCard.deckone(ar)
        playerTwo = newCard.decktwo(br)
        # print(f"player one pulls card number {playerOne}")
        # print(f"player two pulls card number {playerTwo}")
        # print('----------------------')
        if card == 'yes':

            if playerOne == playerTwo:
                holding.append(playerOne)
                holding.append(playerTwo)
                print(
                    f'It is a draw, please pull again \nAfter play, player one has {len(ar)} cards while player two has {len(br)} cards')
                shuffle(ar)
                continue
            elif playerOne > playerTwo:
                # ar.append(hold)

                ar.append(playerOne)
                ar.append(playerTwo)
                # print(holding)
                if len(holding) > 1:
                    ar.extend(holding)
                print(
                    f'after play, player one has {len(ar)} cards while player two has {len(br)} cards')
                continue
            else:
                # ar.append(hold)

                br.append(playerOne)
                br.append(playerTwo)
                # print(holding)
                if len(holding) > 1:
                    br.extend(holding)
                print(
                    f'after play, player one has {len(ar)} cards while player two has {len(br)} cards')
                continue

            continue
        else:
            break
        #     print('not successful')
        # print('hello')
        # print(ar)
        # print(br)
        # print(len(ar))
        # print(len(br))


# if r > t:
#     print('r is bigger')
# else:
#     print ('t is bigger')
#     print(r, t)
