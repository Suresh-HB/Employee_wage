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
PART_TIME_WAGE = 15
PART_TIME_WORKING_HOURS = 8


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


def employee_type_wage_per_day(type_of_employment):
    
    """

    description:
        This function is used to calculate the employee wage based on the type of employment.
    parameters:
        type_of_employment - employee wages will calculating depending upon type of employment
    return:
        employee_wage_per_day, else : enter correct employee_type

    """    

    if type_of_employment == 1:
        employee_wage_per_day = WAGE_PER_HOUR * FULL_DAY_WORKING_HOURS
        return employee_wage_per_day    
    
    else:
        employee_wage_per_day = PART_TIME_WAGE * PART_TIME_WORKING_HOURS
        return  employee_wage_per_day
    

def calculate_employee_monthly_wage():

    """
    description:
        This function is used to calculate monthly wage.
    parameters:
        None
    return:
        employee_monthly wage
    """

    employee_atd_lst = []
    employee_daily_wage =[]
    working_days = 1
    total_wage = 0

    while working_days<=20:

        attendance = check_attendance()
        employee_atd_lst.append(attendance)

        if attendance == 'present':

            emp_type = random.randint(0,1)
            one_day_wage = employee_type_wage_per_day(emp_type)
            employee_daily_wage.append(one_day_wage)
            total_wage+=one_day_wage
        else:
            employee_daily_wage.append(0)
            total_wage+=0
        working_days+=1
    return total_wage, employee_atd_lst, employee_daily_wage


def main():
    
    total_wage, employee_atd_lst, employee_daily_wage = calculate_employee_monthly_wage()
    print(f'Employee 20 days attendance is {employee_atd_lst}')
    print(f'Employee daily wage for 20 days is {employee_daily_wage}')
    print(f'Total monthly wage of employee is {total_wage}') 


if __name__ == '__main__':
    main()