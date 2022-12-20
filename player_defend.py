def defend(self, attack):
    defending_card = None
    if len(self.field) > 0:
        # Select a card to defend with
        print("Select a card to defend with:")
        for i, card in enumerate(self.field):
            print(f"{i}: {card}")
        choice = int(input())
        defending_card = self.field[choice]

    # Calculate the damage
    damage = attack - (defending_card.defense if defending_card is not None else 0)

    # Remove the defending card from the field and reduce the player's life points by the damage
    if damage > 0:
        self.life_points -= damage
        if defending_card is not None:
            self.field.remove(defending_card)
            print(f"{defending_card} was destroyed and ")
        print(f"player{self.player_number} took {damage} damage")

    else:
        print("Defended, no damage taken")

"""
def defend(self, attacking_card, defending_card=None):
    # If the player doesn't specify a defending card,
    # choose the first available card on the field to defend
    if defending_card is None:
        if len(self.field) > 0:
            defending_card = self.field[0]
        else:
            print("No cards on the field to defend with")
            return

    # Check if the defending card is still alive (has positive defense)
    if defending_card.defense <= 0:
        print("{} has no defense left and cannot defend".format(defending_card.name))
        return

    # Calculate the damage taken by the defending card
    damage = max(0, attacking_card.attack - defending_card.defense)

    # Reduce the defense of the defending card by the damage taken
    defending_card.defense = max(0, defending_card.defense - damage)

    # If the defending card has no defense left, it dies
    if defending_card.defense == 0:
        print("{} has been destroyed".format(defending_card.name))
        self.field.remove(defending_card)

    # Print the result of the attack
    print("{} attacks {} for {} damage".format(attacking_card.name, defending_card.name, damage))
"""