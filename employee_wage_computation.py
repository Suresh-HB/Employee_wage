"""

@Author: Suresh
@Date: 2024-07-20
@Last Modified by: Suresh
@Last Modified time: 2024-07-20
@Title : Employee wage computation.

"""
import random

class Employee:

    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4
    WORKING_DAYS_PER_MONTH = 20
    MAX_WORKING_HOURS = 100

    def __init__(self, name, wage_per_hr):
        self.emp_name = name
        self.wage_per_hr = wage_per_hr
        self.total_hrs_worked = 0
        self.total_days_worked = 0
        self.total_wage = 0    
    
    @staticmethod    
    def get_attendance():
        return random.randint(0, 2)
    
    
    def daily_wage(self):
        emp_status = self.get_attendance()
        # print(f"{self.emp_name} attendance status: {emp_status}")  
        
        if emp_status == 0:
            return 0, 0
        elif emp_status == 1: 
            return self.wage_per_hr * self.FULL_DAY_HOURS, self.FULL_DAY_HOURS
        elif emp_status == 2:
            return self.wage_per_hr * self.PART_TIME_HOURS, self.PART_TIME_HOURS
            
    def monthly_wage(self):
        while self.total_days_worked < self.WORKING_DAYS_PER_MONTH and self.total_hrs_worked < self.MAX_WORKING_HOURS:
            wage, hours = self.daily_wage()
            self.total_wage += wage
            self.total_hrs_worked += hours
            self.total_days_worked += 1

    def get_emp_details(self):
        print(f"Name: {self.emp_name}")
        print(f"Total Wage: {self.total_wage}") 
        print(f"Total Hours Worked: {self.total_hrs_worked}")
        print(f"Total Days Worked: {self.total_days_worked}")



def main():
    random.seed()
    
    emp1 = Employee("suresh", 20)
    emp1.monthly_wage()

    emp2 = Employee("ramesh", 30)
    emp2.monthly_wage()

    emp1.get_emp_details()
    emp2.get_emp_details()


if __name__ == '__main__':
    main()
