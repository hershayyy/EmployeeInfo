#Josh Yurche
#This is a program that will display employee information such as Name, date hired, annual salary, 
#Date hired, and social security number

import re

#This is the parent class
class Employee:
    #The constructor has the attributes that all employees will have
    def __init__(self, name, ssn, year, month, date):
        self.name = name
        self.ssn = ssn
        self.year = year
        self.month = month
        self.date = date

    def calcSalary(self, salary):
        self.salary = salary
    #This will display the employee's information
    def displayEmployee(self):
        print("Name: " + self.name + "\nAnnual salary: " \
               + str(self.salary) + "\nDate Hired: " + str(self.date) \
               + " " + self.month + " " + str(self.year) \
               + "\nSSN: " + str(self.ssn))
    
#This is a child/subclass of Employee.  The only change is how salary is calculated
class HourlyEmployee(Employee):
    totalHours = 0.0
    rate = 0.0
    #Overriding the calcSalary method from Employee  
    def calcSalary(self, totalHours, rate):
        self.salary = totalHours * rate
        return(self.salary)
        

class SalariedEmployee(Employee):
    bonus = 0.0
    #Overriding the calcSalary method from Employee
    def calcSalary(self, salary, bonus):
        self.salary = salary + bonus
        return(self.salary)


if __name__ == "__main__":
    print("Testing HourlyEmployee class")
    he = HourlyEmployee("Zoe Sophia", "666-33-4444", 2013, "February", 15)
    he.calcSalary(2080, 95.25)
    print("Employee Details: \n")
    he.displayEmployee()
    print("\nChange the number of hours worked to 3000: \n")
    he.calcSalary(3000,95.25)
    he.displayEmployee()
    print("\n\nTesting SalariedEmployee class")
    se = SalariedEmployee("Reagan Michaela", "222-33-7789", 2014, "June", 1)
    se.calcSalary(85000, 10000)
    print("Employee Details: \n")
    se.displayEmployee()
    print("\nChange the bonus to 15000: \n")
    se.calcSalary(85000, 15000)
    se.displayEmployee()
    
    
    
    
    
