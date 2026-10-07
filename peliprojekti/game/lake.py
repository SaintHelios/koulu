from .fish import Fish

class Lake:
    def __init__(self):
        self.fishes = []
        for i in range(10):
            self.fishes.append(Fish())
