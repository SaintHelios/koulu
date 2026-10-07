from .fish import Fish

class Lake:
    def __init__(self):
        self.fishes = []
        for i in range(20):
            self.fishes.append(Fish())

    def calculate_weight():
        total = 0
        for fish in fishes:
            total += fish.weight
        return total
