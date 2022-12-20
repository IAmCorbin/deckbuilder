# Reset the has_attacked attribute of each card on the field at the end of each turn
def reset_cards(self):
    for card in self.field:
        card.has_attacked = False