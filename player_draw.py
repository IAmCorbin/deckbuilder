import random

# Draw a card from the player's deck
def draw_card(self):
    # If the draw pile is empty, shuffle the discard pile and use it as the new draw pile
    if not self.draw_pile:
        if not self.discard_pile:
            print("No Cards to Draw")
            return
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        random.shuffle(self.draw_pile)

    # Draw a card from the top of the draw pile and add it to the hand
    card = self.draw_pile.pop(0)
    self.hand.append(card)

    # Print the card information
    print(f"Drew card: {card}")

