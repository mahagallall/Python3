import json
from Employee import Employee
from Car import Car

class Office:
    employeesNum = 0  

    def __init__(self, name):
        self.name = name
        self.employees = []  

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        return next((emp for emp in self.employees if emp.id == emp_id), None)

    def hire(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            Office.employeesNum += 1
        else:
            print("Invalid employee object!")

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1
            return True
        return False

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp and deduction > 0:
            emp.money = max(0, emp.money - deduction)  
        else:
            print("Invalid deduction amount or employee not found.")

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp and reward > 0:
            emp.money += reward
        else:
            print("Invalid reward amount or employee not found.")

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if emp:
            targetHour = 9  
            distance = emp.distanceToWork
            velocity = emp.car.velocity if emp.car else 0
            is_late = Office.calculate_lateness(targetHour, moveHour, distance, velocity)

            if is_late:
                print(f"{emp.name} is late! Deducting 10 LE.")
                self.deduct(emp.id, 10)
            else:
                print(f"{emp.name} is on time! Rewarding 10 LE.")
                self.reward(emp.id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        
        if velocity <= 0:  
            return True
        travel_time = distance / velocity
        arrival_time = moveHour + travel_time
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        
        if num >= 0:
            cls.employeesNum = num
        else:
            print("Invalid number of employees.")

def save_office_data_to_json(office, filename="iti_data.json"):
    office_data = {
        "name": office.name,
        "employees": [
            {
                "name": emp.name,
                "money": emp.money,
                "mood": emp.mood,
                "healthRate": emp.healthRate,
                "id": emp.id,
                "car": {
                    "name": emp.car.name,
                    "fuelRate": emp.car.fuelRate,
                    "velocity": emp.car.velocity
                } if emp.car else None,
                "email": emp.email,
                "salary": emp.salary,
                "distanceToWork": emp.distanceToWork
            }
            for emp in office.employees
        ]
    }

    with open(filename, "w") as f:
        json.dump(office_data, f, indent=4)

    print(f"Office data saved to {filename}")
