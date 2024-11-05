class Employee ():

    def calculate_salary(self):
        return "Calculating salary for an employee."

class Manager(Employee):

     def manager_salary(self):
         return "Calculating the managers salary with additional benefits"
           
# Creating an instance of Employee and calling calculate_salary
employee = Employee()
print(employee.calculate_salary()) #should print the generic employee message

# Creating an instance of Manager and calling calculate_salary
manager = Manager()
print(manager.calculate_salary()) #should print the manager_specific massage

