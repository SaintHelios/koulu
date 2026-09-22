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

class ElectricCar(Car):

    def __init__(self, reg, maxspd, cap):
        super().__init__(reg, maxspd)
        self.cap = cap

class GasolineCar(Car):

    def __init__(self, reg, maxspd, lit):
        super().__init__(reg, maxspd)
        self.lit = lit

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ABC-123", 165, 32.2)

electric.accelerate(60)
gasoline.accelerate(70)

for i in range(3):
    gasoline.drive(1)
    electric.drive(1)
print(f"Electric: {electric.distance} Kilometers\nGasoline: {gasoline.distance} Kilometers")
