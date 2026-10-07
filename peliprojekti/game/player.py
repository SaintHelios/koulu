class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bucket = []
        self.day = 1
        self.underage = False
        if age < 18:
            self.underage = True

