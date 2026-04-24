class Employee:
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
    def get_pay(self):
        return self.pay
class Section:
    def __init__(self,name,max_emp):
        self.name=name
        self.max_emp=max_emp
        self.employees=[]
    def add_employee(self,employee):
        if len(self.employees)<self.max_emp:
            self.employees.append(employee)
            return True
        return False 
    def avg_pay(self):
        value=0
        for employee in self.employees:
            value+=employee.get_pay()
        average_val=value/(len(self.employees))
        return average_val 
e1=Employee("manya",18,20000)
e2=Employee("ishaan",18,15000)
e3=Employee("vihaan",18,17000)
sec1=Section("marketing",2)
sec1.add_employee(e1)
sec1.add_employee(e2)
#sec1.add_employee(e3)
print(sec1.employees[1].pay)
print(sec1.avg_pay())
