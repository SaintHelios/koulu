import random

class Fish:

    multiplier = 1
    rarity_tiers = ["Common", "Uncommon", "Rare", "Legendary"]
    fish_weights = [ 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.25, 1.5, 1.8, 2.0, 2.25, 2.5, 2.8, 3.0 ]
    fish_names = [
    "Blue Snake", "Great White Sardine", "Lake Shark", "Majestic Mud Herring", 
    "Striped Moss Sucker", "Swamp Anaconda", "Giant Pebble Goby", "Freshwater Barracuda", 
    "Flying Lake Eel", "Pond Leviathan", "Spotted Water Cobra", "Nordic Neon Guppy", 
    "Golden Reed Viper", "Miniature Whale", "Star Destroyer Tuna", "Intergalactic Anchovy", 
    "Orbital Laser Pike", "Doomsday Guppy", "Tactical Mud Carp", "Nuclear Minnow", 
    "Sub-Zero Salmon", "Hyperdrive Haddock", "Quantum Flounder", "Apex Predator Goldfish", 
    "Mecha-Mackerel", "Galactic Gravel Goby", "Void-Walker Trout", "Death-Ray Ray", 
    "Battle-Cruiser Cod", "Cosmic Krill", "Stealth Bomber Catfish", "Thermo-Nuclear Tilapia"
    ]


    def __init__(self, name=None, weight=None, value=None, rarity=None):

        # if values != None means that the game_load() function called the class
        if name != None and weight != None:
            self.name = name
            self.weight = weight
            self.value = value
            self.rarity = rarity
        else:
            # else initialises a new fish 
            self.name = random.choice(self.fish_names)
            self.weight = random.choice(self.fish_weights)
            self.value = self.weight * 11.50

            # rarity system, fishes gain worth on higher tiers 
            self.rarity = random.choices(self.rarity_tiers, weights = [60, 25, 10, 5])[0]
            if self.rarity == "Uncommon":
                self.multiplier = 2
            elif self.rarity == "Rare":
                self.multiplier = 5
            elif self.rarity == "Legendary":
                self.multiplier = 20
                self.name = f"Golden {self.name}"
                self.weight += 3.0
        
            self.value = self.weight * 11.50 * self.multiplier

        if self.weight < 1:
            self.size = "small"
        else:
            self.size = "big"

        # Peak OOP code 
