import random

class Car:
    def __init__(self, reg, maxspd):
        self.reg = reg
        self.maxspd = maxspd
        self.spd = 0
        self.distance = 0
    
    def accelerate(self, change):
        self.spd += change
         
        if self.spd > self.maxspd:
            self.spd = self.maxspd
        elif self.spd < 0:
            self.spd = 0        
        return self.spd
    
    def drive(self, hours):
        traveled = hours * self.spd
        self.distance += traveled
        return self.distance

class Race:

    def __init__(self, name, distance, participants):
        self.name = name
        self.distance = distance
        self.participants = participants

    def hour_passes(self):
        for i in self.participants:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)
    
    def print_status(self):
        for i in self.participants:
            print(f"Car: {i.reg} : {i.distance}")

    def race_finished(self):
        for i in self.participants:
            if i.distance >= self.distance:
                return True
        return False

tuah = 0                    
cars = []
for i in range(10):
    cars.append(Car("ABC-"+str(i+1), random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

while True:
        race.hour_passes()
        if race.race_finished():
            print(f"\nFinish!\nCurrent hour: {tuah}")
            race.print_status()
            break

        if tuah % 10 == 0:
            print(f"\nCurrent hour: {tuah}")
            race.print_status()
        tuah += 1
