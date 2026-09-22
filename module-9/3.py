class Car:
    def __init__(self, reg, maxspd):
        self.reg = reg
        self.maxspd = maxspd
        self.spd = 0
        self.distance = 0
    
    def accelerate(self, change):
        self.spd += change
         
        if self.spd > self.maxspd:
            print(f"The car speed cannot exceed the maximum speed of {self.maxspd}km/h")
            self.spd = self.maxspd
        elif self.spd < 0:
            print("The car speed cannot be below 0")
            self.spd = 0        
        return self.spd
    
    def drive(self, hours):
        traveled = hours * self.spd
        self.distance += traveled
        return self.distance

NewCar = Car("ABC-123", 142)
NewCar.accelerate(60)
NewCar.drive(1.5)
print(f"\nRegistration: {NewCar.reg:s}\nMax Speed: {NewCar.maxspd:d}km/h\nSpeed: {NewCar.spd:d}km/h\nDistance Driven: {NewCar.distance}\n")

