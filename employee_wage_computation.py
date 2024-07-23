"""

@Author: Suresh
@Date: 2024-07-22
@Last Modified by: Suresh
@Last Modified time: 2024-07-22
@Title : Employee wage computation.

"""

import random

from abc import ABC, abstractmethod


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

        """
        Description: Function to generate attendace using random class.
        Parameters:
            None:
        Returns:
            return: function returns the employee attendence.
        """

        return random.randint(0, 2)
    
    def daily_wage(self):

        """
        Description: Function to calculates employee daily wage.
        Parameters:
            None:
        Returns:
            return: returns the employee wage on work type. 
        """

        emp_status = self.get_attendance()

        if emp_status == 0:
            return 0, 0
        elif emp_status == 1: 
            return self.wage_per_hr * self.FULL_DAY_HOURS, self.FULL_DAY_HOURS
        elif emp_status == 2:
            return self.wage_per_hr * self.PART_TIME_HOURS, self.PART_TIME_HOURS 
        
    def monthly_wage(self):

        """
        Description: Function to calculates employee monthly wage based on the 
            specified working days in a month and working hours.
        Parameters:
            None:
        Returns:
            None:  
        """

        while self.total_days_worked < self.WORKING_DAYS_PER_MONTH and self.total_hrs_worked < self.MAX_WORKING_HOURS:
            wage, hours = self.daily_wage()
            self.total_wage += wage
            self.total_hrs_worked += hours
            self.total_days_worked += 1
   
    def get_emp_details(self):

        """
        Description: Function for prints the employee details.
        Parameters:
            None:
        Returns:
            None:
        """

        print(f"Name: {self.emp_name}")
        print(f"Total Wage: {self.total_wage}") 
        print(f"Total Hours Worked: {self.total_hrs_worked}")
        print(f"Total Days Worked: {self.total_days_worked}")


class Company:
    
    def __init__(self, name) -> None:
        self.company_name = name
        self.employee_dict = {}

    def get_employee(self, emp_name):
 
        """
        Description: Function to gives the employee name from employee_list = [].
        Parameters:
            emp_name: Function taking employee name and return name if it is present.
        Returns:
            return: returns employee name.
        """

        return self.employee_dict.get(emp_name)

    def add_employee(self, emp_obj):
        
        """
        Description: Function to adding employees into company after creating company object.
        Parameters:
            emp_obj: Function taking employee object for adding it in to company.
        Returns:
            None: 
        """

        self.employee_dict.update({emp_obj.emp_name: emp_obj})

    def delete_employee(self, emp_name):
        
        """
        Description: Function to delete employee from company.
        Parameters:
            emp_name: Function taking employee name and delete employee based on name.
        Returns:
            None: 
        """

        self.employee_dict.pop(emp_name)
    
    def display_emp_details(self):
        
        """
        Description: Function for prints the employee details.
        Parameters:
            None:
        Returns:
            None:  
        """

        for emp in self.employee_dict.values():
            emp.get_emp_details()
            print("="*50)      

from abc import ABC, abstractmethod


class EmployeeWageBuilder(ABC):

    """
    Abstract base class for managing employee wage information for multiple companies.
    This class defines methods for managing companies and their associated wage data.
    """

    @abstractmethod
    def get_company(self, comp_name):
        """Retrieve details of a company based on its company name."""
        pass

    @abstractmethod
    def add_company(self, com_obj):
        """Add a new company object."""
        pass

    @abstractmethod
    def delete_company(self, company_name):
        """Delete a company and its associated wage information from the company."""
        pass
    
    @abstractmethod
    def display_company(self):
        """Display all companies currently managed in the company."""
        pass


class MultipleCompanies(EmployeeWageBuilder):
     
    """
    Concrete implementation of EmployeeWageBuilder interface for managing multiple companies wage information.
    """

    def __init__(self) -> None:
        
        """ Initialize MultipleCompanies with an empty dictionary to store company objects."""
        self.company_dict = {} 

    def get_company(self, comp_name):
        
        """
        Description: Retrieve details of a company based on its name.
        Parameters:
            comp_name: Function taking company name as a parameter and retrieve Name of the company.
        Returns:
            Company object or None: the company object if found in company_list = [], else returns None.
        """
        if comp_name not in self.company_dict:
            return None
        return self.company_dict[comp_name]
        

    def add_company(self, com_obj):
        
        """
        Description: Add a new company object .
        Parameters:
            com_obj: Company An instance of the Company class representing the company to add.
        Returns:
            None:
        """

        self.company_dict.update({com_obj.company_name: com_obj})
        print(f"Employee added to {com_obj.company_name} Successfully")

    def delete_company(self, company_name):

        """
        Description: Delete a company and its associated wage information from the company.
        Parameters:
            company_name: Name of the company to delete from company_dict.
        Returns:
            None:
        """

        self.company_dict.pop(company_name)

    def display_company(self):
        
        """
        Description: Display all companies currently managed in the company.
        Parameters:
            None:
        Returns:
            None:
        """
        
        for com in self.company_dict.values():
            print(f"Company: {com.company_name}")
            com.display_emp_details()
    
def main():
    
    print("---------------------------------------------------")
    print("|   ***  WELCOM TO EMPLOYEE WAGE COMPUTATION  ***  |")
    print("---------------------------------------------------")
    
    multi_comp = MultipleCompanies()
    while True:

        print("       Menu")
        print("      ======")
        print("choice 1: To add company")
        print("choice 2: To display company")
        print("choice 3: To delete company")
        print("choice 4: To delete employee")
        choice = int(input("**Enter Your Choice**\n"))
        
        match choice:
            case 0:
                break
        
            case 1:
                company_name = input("Enter company name: ")
                company = multi_comp.get_company(company_name)
                if not company:
                    company = Company(company_name)
                    emp_name = input("Enter employee name: ")
                    employee = company.get_employee(emp_name)
                    
                if not employee:
                    wage_per_hr = int(input("Enter wage: "))
                    employee = Employee(emp_name, wage_per_hr)
                    employee.monthly_wage()
                    company.add_employee(employee)
                    multi_comp.add_company(company)
            
            case 2:
                multi_comp.display_company()

            case 3:
                company_name = input('Enter company name to delete: ')
                multi_comp.delete_company(company_name)

            case 4:
                company_name = input("Enter company name: ")
                company = multi_comp.get_company(company_name)
                
                if not company:
                    print("Company not found")
                    continue
                emp_name = input('Enter employee name to delete: ')
                company.delete_employee(emp_name)


if __name__ == '__main__':
    main()