def attack(self, card_name, target_player):
    # Find the card in the player's field
    attacking_card = None
    for card in self.field:
        if card.name == card_name:
            attacking_card = card
            break

    # Check if the card was found and if it has already attacked this turn
    if attacking_card is None:
        print("Invalid card name")
    elif attacking_card.has_attacked:
        print("This card has already attacked this turn")
    else:
        # Set the card's has_attacked attribute to True
        attacking_card.has_attacked = True

        # Attack the target player
        target_player.defend(attacking_card.attack)


"""
from attack_target import AttackTarget

# Attack with a card on the field
def attack(self, card_name, target_player=None, target_card=None):
    # Find the card with the given name in the player's field
    card = None
    for c in self.field:
        if c.name == card_name:
            card = c
            break

    # If the card was not found, print an error message and return
    if not card:
        print("Invalid card name")
        return

    # Create an AttackTarget object using the provided target player or card
    target = AttackTarget(player=target_player, card=target_card)

    # Check if the card is able to attack this turn
    if card.has_attacked:
        print("This card has already attack this turn")
        return

    # Mark the card as having attack this turn
    card.has_attacked = True

    # Decrease the target's life points by the attack value of the attacking card
    if target.player:
        target.player.life_points -= card.attack
    if target.card:
        target.card.defense -= card.attack
        if target.card.defense <= 0:
            target.card = None

    # If the target's life points are less than or equal to zero, the game is over
    if target.player and target.player.life_points <= 0:
        print(f"Game over player {target.player.player_number}!")
        return

"""