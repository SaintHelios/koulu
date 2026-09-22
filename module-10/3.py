class Elevator:

    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = self.bottom

    def floor_up(self):
        self.floor += 1
        print(f"{self.floor} up")
        

    def floor_down(self):
        self.floor -= 1
        print(f"{self.floor} down")

    def go_to_floor(self, reps):
        self.reps = reps
        
        while self.floor != reps:
            if self.floor < reps and self.floor < self.top:
                self.floor_up()
            elif self.floor > reps and self.floor > self.bottom:
                self.floor_down()
            else:
                print(f"Floor {reps} is an invalid floor")
                break

class Building:

    def __init__(self, bottom, top, tri):
        self.bottom = bottom
        self.top = top
        self.tri = tri
        self.elevators = []

        for i in range(tri):
            elevator = Elevator(self.bottom, self.top)
            self.elevators.append(elevator)
            
    def run_elevator(self, bi, floor):
        self.bi = bi
        self.floor = floor
        
        self.elevators[bi].go_to_floor(floor)

    def firealarm(self):
        for _ in self.elevators:
            _.go_to_floor(self.bottom)

meow = Building(1, 10, 2)
meow.run_elevator(1, 5)
meow.firealarm()
print(meow.elevators[1].floor)

