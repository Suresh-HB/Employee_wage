"""

@Author: Suresh
@Date: 2024-07-19
@Last Modified by: Suresh
@Last Modified time: 2024-07-19
@Title : Employee wage computation.

"""


import random


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


def main():

    attendance = check_attendance()
    print("Employee is ",attendance)


if __name__ == '__main__':
    main()