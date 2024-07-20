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
WORKING_DAYS_PER_MONTH = 20

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

    if type_of_employment == 'FULL-TIME':
        employee_wage_per_day = WAGE_PER_HOUR * FULL_DAY_WORKING_HOURS
        return employee_wage_per_day
    
    elif type_of_employment == 'PART-TIME':
        employee_wage_per_day = PART_TIME_WAGE * PART_TIME_WORKING_HOURS
        return employee_wage_per_day
    
    else:
        return "enter valid employee_type(FULL-TIME/PART-TIME)"
    

def main():

    attendance = check_attendance()
    print("Employee is ",attendance)
    wage_per_day = 0

    if attendance == 'present':
        type_of_employment = input("enter FULL-TIME/PART-TIME: ").upper()
        wage_per_day = employee_type_wage_per_day(type_of_employment)
        print(f"employee wage  = {wage_per_day}")
    else:
        print(f"employee wage  = {wage_per_day}")

        
if __name__ == '__main__':
    main()