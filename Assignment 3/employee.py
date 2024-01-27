class Employee:
    # Class variable to count the number of Employees
    employee_count = 0
    
    def __init__(self, name, family, salary, department):
        # Instance variables
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        
        # Increment the employee count
        Employee.employee_count += 1
    
    def average_salary(self, *salaries):
        # Calculate and return the average salary
        total_salary = sum(salaries) + self.salary
        num_employees = len(salaries) + 1 
        return total_salary / num_employees


class FullTimeEmployee(Employee):
    # FullTimeEmployee class inheriting from Employee class
    def __init__(self, name, family, salary, department, bonus):
        # Call the constructor of the parent class
        super().__init__(name, family, salary, department)
        self.bonus = bonus


# Creating instances of Employee and FullTimeEmployee
employee1 = Employee("Ethan Hunt", "Family1", 50000, "HR")
employee2 = Employee("Julie Hunt", "Family2", 60000, "Finance")

full_time_employee = FullTimeEmployee("Benji Gozales", "Family3", 70000, "IT", 10000)

# Calling member functions
average_salary_all = employee1.average_salary(employee2.salary)
average_salary_full_time = full_time_employee.average_salary()

print(f"Total number of employees: {Employee.employee_count}")
print(f"Average salary for all employees: {average_salary_all}")
print(f"Average salary for FullTimeEmployee: {average_salary_full_time}")
