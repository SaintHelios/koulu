import random

class Fish:

    fish_weights = [ 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.25, 1.5, 1.8, 2.0, 2.25, 2.5, 2.8, 3.0 ]
    fish_names = ["Blue Snake", "Great White Sardine", "Lake Shark", "Majestic Mud Herring", "Striped Moss Sucker", "Swamp Anaconda", "Giant Pebble Goby", "Freshwater Barracuda", "Flying Lake Eel", "Pond Leviathan", "Spotted Water Cobra", "Nordic Neon Guppy", "Golden Reed Viper", "Miniature Whale"]

    def __init__(self):
        self.name = random.choice(self.fish_names)
        self.weight = random.choice(self.fish_weights)

        if self.weight < 1:
            self.size = "small"
        else:
            self.size = "big"
            
