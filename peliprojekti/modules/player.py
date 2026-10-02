class Player:
    def __init__(self, name: str, location):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, direction: str) -> bool:
        direction = direction.lower()
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"\nLiikuittiin suuntaan '{direction}'.")
            return True
        else:
            print(f"\nSuuntaan '{direction}' ei pääse täältä!")
            return False

    def collect_item(self) -> bool:
        if self.location.item:
            item = self.location.remove_item()
            self.inventory.append(item)
            print(f"\nKeräsit esineen: {item}")
            return True
        else:
            print("\nTässä huoneessa ei ole kerättävää esinettä.")
            return False

    def show_inventory(self):
        if not self.inventory:
            print("\nTavarasäiliösi on tyhjä.")
        else:
            print("\n--- Tavarasäiliösi sisältö ---")
            for item in self.inventory:
                print(f" - {item}")
