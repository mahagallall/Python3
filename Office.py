import json
from Employee import Employee

class Office:
    employeesNum = 0
    
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, empId):
        return next((emp for emp in self.employees if emp.emp_id == empId), None)
    
    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
    
    def fire(self, empId):
        self.employees = [emp for emp in self.employees if emp.emp_id != empId]
        Office.employeesNum -= 1
    
    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
    
    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
    
    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            lateness = self.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if lateness:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)
    
    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        return (moveHour + distance / velocity) > targetHour
    
    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num
    
    def save_to_json(self):
        with open("office_data.json", "w") as f:
            json.dump([emp.__dict__ for emp in self.employees], f)
