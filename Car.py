class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        if not (0 <= velocity <= 200):
            print("Invalid velocity. Velocity must be between 0 and 200.")
            return

        if not (0 <= self._fuelRate <= 100):
            print("Invalid fuel rate. Fuel rate must be between 0 and 100.")
            return

        self._velocity = velocity
        fuel_consumption = distance / 10

        if self._fuelRate >= fuel_consumption:
            self._fuelRate -= fuel_consumption
            self.stop(0)
        else:
            remaining_distance = self._fuelRate * 10
            self._fuelRate = 0
            self.stop(distance - remaining_distance)


    def refuel(self, amount):
       
        if amount > 0:
            self._fuelRate = min(100, self._fuelRate + amount)
        else:
            print("Invalid refuel amount.")

    def stop(self, remaining_distance):
        self._velocity = 0
        if remaining_distance == 0:
            print("Arrived at the destination.")
        else:
            print(f"Stopped. Remaining distance: {remaining_distance} km.")

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("Invalid velocity. Velocity must be between 0 and 200.")

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if 0 <= value <= 100:
            self._fuelRate = value
        else:
            print("Invalid fuel rate. Fuel rate must be between 0 and 100.")
