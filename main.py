import random
from card import Card
from player import Player

# Create a deck of cards
deck1 = [
    Card("Goblin", 1, 2, 1),
    Card("Orc", 2, 3, 2),
    Card("Troll", 3, 4, 3),
    Card("Giant", 6, 8, 5),
]

deck2 = [
    Card("Goblin", 1, 2, 1),
    Card("Orc", 2, 3, 2),
    Card("Troll", 3, 4, 3),
    Card("Giant", 6, 8, 5),
]

# Shuffle the deck
random.shuffle(deck1)
random.shuffle(deck2)

# Create two players
player1 = Player(1, deck1)
player2 = Player(2, deck2)

# Main game loop
while True:
    # Start player 1's turn
    player1.start_turn(target_player=player2)

    # Check if the game is over
    if player2.life_points <= 0:
        print("Player 1 wins!")
        break

    # Start player 2's turn
    player2.start_turn(target_player=player1)

    # Check if the game is over
    if player1.life_points <= 0:
        print("Player 2 wins!")
        break
