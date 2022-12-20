def print_info(self):
    print(f"Player {self.player_number}'s turn")

    print("\nHand:")
    for card in self.hand:
        print(card)

    print("\nField:")
    for card in self.field:
        print(card)

    print(f"\nHP[{self.life_points}] | Mana[{self.mana_points}]")