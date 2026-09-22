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
            

h = Elevator(1, 10)

h.go_to_floor(10)
h.go_to_floor(11)
h.go_to_floor(1)
h.go_to_floor(-2)
