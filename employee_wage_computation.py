"""

@Author: Suresh
@Date: 2024-07-19
@Last Modified by: Suresh
@Last Modified time: 2024-07-19
@Title : Employee wage computation.

"""


import random

WAGE_PER_HOUR = 20  
FULL_DAY_WORKING_HOURS = 8


def check_attendance():

    """
    description:
        This function is used to check employee attendance.
    parameters:
        None
    return:
        employee_attendance
    """    


    attendance = random.randint(0, 1)

    if attendance == 1:
        employee_attendance = 'present'

    else:
        employee_attendance = 'absent'
    
    return employee_attendance


def DailyEmployeeWage(attendance):
    """
    description:
        This function is used to calculate employee wage for full time employees.
    parameters:
        attendance - to calculate the wage based on the employee presence
    return:
        employee_wage_per_day
    """


    if attendance == 'present':
        emp_wage_per_day = WAGE_PER_HOUR * FULL_DAY_WORKING_HOURS
    else:
        emp_wage_per_day = 0
    
    return emp_wage_per_day


def main():

    attendance = check_attendance()
    print("Employee is ",attendance)

    emp_day_wage = DailyEmployeeWage(attendance)
    print(f'Employee daily wage is {emp_day_wage}')


if __name__ == '__main__':
    main()