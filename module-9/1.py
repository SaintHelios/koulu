class Car:
    def __init__(self, reg, maxspd):
        self.reg = reg
        self.maxspd = maxspd
        self.spd = 0
        self.distance = 0
        

NewCar = Car("ABC-123", 142)
print(f"\nRegistration: {NewCar.reg:s}\nMax Speed: {NewCar.maxspd:d}km/h\nSpeed: {NewCar.spd:d}\nDistance Driven: {NewCar.distance:d}\n")

