class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bucket = []
        self.day = 1

    def calculate_weight(self):
        total = 0
        for fish in self.bucket:
            total += fish.weight
        return total

    def list_fish(self):
        index = 1
        print(f"\n\t~~~ ""{ Silly Bucket }"" ~~~")
        for fish in self.bucket:
            print(f"\t Fish {index}~ {fish.rarity} {fish.name}, {fish.weight}kg")
            index += 1
        print(f"\t Total bucket weight: {self.calculate_weight()}kg\n")
