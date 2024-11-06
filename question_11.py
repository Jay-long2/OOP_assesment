
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self,employee):
        self.employee.append(employee)
    
    def total_payroll(self):
        return sum(employee.salary for employee in self.employees)
    
emp1 = Employee("mark", "40000")
emp2 = Employee("Jack","400503")
print(f"{emp1.name} {emp1.salary}")
print(f"{emp2.name} {emp1.salary}")
payroll1 = Payroll()
payroll1.add_employee(emp1)
payroll1.add_employee(emp2)
print(f"Total Payroll {payroll1.total_payroll()}")


