import re
from Person import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self._email = None  
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.email = email  
   
    def work(self, hours):
       
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"
    def drive(self, distance):
        if self.car:
            self.car.run(self.car.velocity, distance)
        else:
            print("This employee has no car to drive.")

     
    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if self.is_valid_email(value):  
            self._email = value
        else:
            print("Invalid email address.")
    
    
