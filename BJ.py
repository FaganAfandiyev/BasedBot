import random
import os
from BasedBot import BasedBot
from wrappers import command, listen
import signal

lastID = "a"
#signal handler
def handler(signum, frame):
    bot.send('md20m', "Forever is over!")
    raise Exception("end of time")

basedBot = BasedBot()

bot = BasedBot()
# Define card values
card_values = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

# Define deck of cards
deck = list(card_values.keys()) * 4

# Define a function to deal a card
def deal_card():
    return deck.pop(random.randint(0, len(deck)-1))

# Define a function to calculate the score of a hand
def calculate_score(hand):
    score = sum([card_values[card] for card in hand])
    if score > 21 and 'Ace' in hand:
        score -= 10
    return score

# Define the main game function
async def play_game(playerName, chat):
    # Shuffle the deck
    lastID = "id"
    lastIDFeqan = "id"
    random.shuffle(deck)

    # Deal initial cards
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Show player's hand and one of the dealer's cards
    score = calculate_score(player_hand)
    bot.send(chat, f"Player's hand: {player_hand}  {score}")
    bot.send(chat, f"Dealer's hand: [{dealer_hand[0]}, _ ]")

    # Player's turn
    while True:
        score = calculate_score(player_hand)
        if score == 21:
            bot.send(chat, "Blackjack! You win!")
            return
        elif score > 21:
            bot.send(chat, "Bust! You lose.")
            return
        else:

            if (basedBot.message_id(chat) == lastIDFeqan): 
              lastIDFeqan == basedBot.message_id(chat)
              continue
            else: 
             bot.send(chat, "Would you like to hit or stand?")
             lastIDFeqan == basedBot.message_id(chat)
            #lastID = basedBot.message_id(chat)
            print(basedBot.message_id(chat), lastID, basedBot.message_sender_name(chat) == playerName)
            if (basedBot.message_id(chat) != lastID and basedBot.message_sender_name(chat) == playerName): 
              response = basedBot.message_text(chat)
              print(response)
              if response.lower() == 'hit':
                player_hand.append(deal_card())
                score = calculate_score(player_hand)
                bot.send(chat, f"Player's hand: {player_hand} {score}")
                lastID = basedBot.message_id(chat)
              else:
                break

    # Dealer's turn
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # Show the final hands
    bot.send(chat, f"Player's hand: {player_hand} ({calculate_score(player_hand)})")
    bot.send(chat, f"Dealer's hand: {dealer_hand} ({calculate_score(dealer_hand)})")

    # Determine the winner
    if dealer_score > 21:
        bot.send(chat, "Dealer busts! You win!")
    elif dealer_score == calculate_score(player_hand):
        bot.send(chat, "It's a tie!")
    elif dealer_score > calculate_score(player_hand):
        bot.send(chat, "Dealer wins!")
    else:
        bot.send(chat, "You win!")


# Register Signal Function Handler
signal.signal(signal.SIGALRM, handler)
signal.alarm(35)
# Call the main game function
async def blackjack(playerName, chat):
 await play_game(playerName, chat)