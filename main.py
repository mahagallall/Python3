from Person import Person
from Employee import Employee
from Car import Car
from Office import Office


car1 = Car("Fiat128", 80, 60)
employee1 = Employee("Lila", 5000, "happy", 100, 1, car1, "lila@iti.com", 2000, 20)
office = Office("ITI")
office.hire(employee1)
office.save_to_json()
