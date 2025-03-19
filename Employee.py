from Person import Person
from Car import Car

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.emp_id = emp_id
        self.car = car
        self.email = email if "@" in email else "Invalid Email"
        self.salary = max(1000, salary)
        self.distanceToWork = distanceToWork
    
    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
    
    def drive(self, distance):
        self.car.run(self.car.velocity, distance)
    
    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)
    
    def send_mail(self, to, subject, msg, receiver_name):
        with open("email.txt", "w") as f:
            f.write(f"From: {self.email}\nTo: {to}\nHi, {receiver_name}\n{msg}\nSubject: {subject}")
