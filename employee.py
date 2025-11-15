class Employee:
    def __init__(self,name,firstName,grade,baseSalary,taxes):
        self.name=name
        self.firstName=firstName
        self.grade=grade
        self.baseSalary=baseSalary
        self.taxes=taxes
    def calculate_net_salary(self):
        return self.baseSalary - (self.baseSalary * self.taxes / 100)
    def display_employee_info(self):
        net_salary=self.calculate_net_salary()
        return (f"Employee: {self.firstName} {self.name}, Grade: {self.grade}, "
                f"Base Salary: {self.baseSalary}, Taxes: {self.taxes}%, "
                f"Net Salary: {net_salary}")