class Room:
    def __init__(self, name: str, description: str = "", item=None):
        self.name = name
        self.description = description
        self.item = item
        self.exits = {}  # esim. {"pohjoinen": huone_objekti}

    def add_exit(self, direction: str, room):
        self.exits[direction.lower()] = room

    def remove_item(self):
        item = self.item
        self.item = None
        return item

    def __str__(self) -> str:
        info = f"=== {self.name} ===\n{self.description}"
        if self.item:
            info += f"\nHuoneessa on esine: {self.item}"
        else:
            info += "\nHuoneessa ei ole irtoesineitä."
        if self.exits:
            info += f"\nIlmansuunnat, joihin voit liikkua: {', '.join(self.exits.keys())}"
        return info
