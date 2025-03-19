class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = max(0, min(fuelRate, 100))
        self.velocity = max(0, min(velocity, 200))
    
    def run(self, velocity, distance):
        self.velocity = velocity
        self.fuelRate -= distance * 10 / 100
        if self.fuelRate <= 0:
            self.stop()
        else:
            print(f"Car is running. Remaining fuel: {self.fuelRate}%")
    
    def stop(self):
        self.velocity = 0
        print("Car has stopped.")
