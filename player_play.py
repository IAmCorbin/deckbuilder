# Play a card from the player's hand
def play_card(player, card_name):
    # Find the card with the given name in the player's hand
    card = None
    for c in player.hand:
        if c.name == card_name:
            card = c
            break

    # If the card was not found, print an error message and return
    if not card:
        print("Invalid card name")
        return

    # Check if the player has enough mana to play the card
    if player.mana_points < card.cost:
        print("Not enough mana to play this card")
        return

    # Remove the card from the hand and add it to the field
    player.hand.remove(card)
    player.field.append(card)

    # Reduce the player's mana points by the cost of the card
    player.mana_points -= card.cost

    # Print the card information
    print(f"Played card: {card}")
