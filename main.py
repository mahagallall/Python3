from Person import Person
from Employee import Employee
from Car import Car
from Office import Office, save_office_data_to_json 


person1 = Person("Maha", 500, "Happy", 100)
person1.sleep(6)
print(f"Mood after sleeping: {person1.mood}")  
person1.eat(2)
print(f"Health Rate after eating: {person1.healthRate}%")  
person1.buy(4)
print(f"Money after buying items: {person1.money} LE")  


my_car = Car("Marcdez-Benz", 50, 120)


employee1 = Employee("Maha", 5000, "Happy", 90, 101, my_car, "maha@yahoo.com", 1200, 15)
employee1.drive(10)
print(f"Remaining Fuel after driving: {employee1.car.fuelRate}%")
employee1.car.refuel(30)
print(f"Fuel after refueling: {employee1.car.fuelRate}%")
employee1.work(9)
print(f"My mood after working: {employee1.mood}") 


iti = Office("ITI")
iti.hire(employee1)


iti.check_lateness(101, moveHour=8)


save_office_data_to_json(iti)
