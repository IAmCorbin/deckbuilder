# Import the card and attack_target modules
from card import Card
from attack_target import AttackTarget

# Import the player_hand, player_mana, player_draw, and player_attack modules
import player_play
import player_turn
import player_draw
import player_attack
import player_defend
import player_reset
import player_print

# Create the Player class
class Player:
    def __init__(self, playerNumber, deck):
        self.player_number = playerNumber
        self.deck = deck
        self.hand = []
        self.field = []
        self.life_points = 20
        self.mana_points = 0
        self.draw_pile = deck.copy()
        self.discard_pile = []

    # Add the start_turn method from the player_mana module
    start_turn = player_turn.start_turn

    # Add the draw_card method from the player_draw module
    draw_card = player_draw.draw_card

    # Add the play_card method from the player_hand module
    play_card = player_play.play_card

    # Add the attack method from the player_attack module
    attack = player_attack.attack

    # Allow players to defend themselves
    defend = player_defend.defend

    reset_cards = player_reset.reset_cards

    print_info = player_print.print_info
