class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bucket = []
        self.day = 1
        self.underage = False
        if age < 18:
            self.underage = True

    def calculate_weight(self):
        total = 0
        for fish in self.bucket:
            total += fish.weight
        return total

    def list_fish(self):
        index = 1
        for fish in self.bucket:
            print(f"Fish {index}~ {fish.name}, {fish.weight}kg")
            index += 1
        print(f"Total bucket weight: {self.calculate_weight()}kg")
