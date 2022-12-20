def start_turn(self, target_player):
    self.mana_points += 1
    self.draw_card()
    self.reset_cards()
    self.print_info()

    while True:
        # Prompt the player for input
        action = input("Enter a command (play, attack, info, end turn): ")

        # Split the action into the command and the card name
        action_parts = action.split()
        command = action_parts[0]
        card_name = None
        if len(action_parts) > 1:
            card_name = " ".join(action_parts[1:])

        # Determine which action to take based on the input
        if command == "play":
            self.play_card(card_name)
        elif command == "attack":
            self.attack(card_name, target_player=target_player)
        elif command == "info":
            self.print_info()
        elif command == "end":
            # End the current player's turn
            break
        else:
            print("Invalid command")

