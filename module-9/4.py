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

cars = []
for i in range(10):
    cars.append(Car("ABC-"+str(i+1), random.randint(100, 200)))
meow = 0
while meow != 1:
    for i in cars:
        i.accelerate(random.randint(-10, 15))
        i.drive(1)
        
        if i.distance >= 10000:
            meow = 1
for i in cars:
    print(f"Car: {i.reg} : {i.distance}")
