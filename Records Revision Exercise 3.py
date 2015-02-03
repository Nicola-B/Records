#Nicola Batty
#30/01/2015
#Records Revision Exercise 3

class employee_pay_slip:
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None
        self.total_pay = None

def calculat_total_pay(hours_worked, rate_of_pay):
    total_pay = rate_of_pay * hours_worked
    return total_pay

def input_data():
    employee = employee_pay_slip()
    employee.name = input("Please input the employee's name: ")
    employee.number = input("Please input the employee's number: ")
    employee.hours = int(input("Please input the number of hours the employee has worked this week: "))
    employee.pay = int(input("Please input the employee's rate of pay: "))
    employee.total_pay = calculat_total_pay(employee.hours, employee.pay)
    return employee

def display_data(employee):
    print("*"*40)
    print("* {0:<36} *".format("Pay Slip"))
    print("* {0:<36} *".format(" "))
    print("* Name: {0:<30} *".format(employee.name))
    print("* Employee Number: {0:<19} *".format(employee.number))
    print("* Hours Worked: {0:<22} *".format(employee.hours))
    print("* Rate of pay: £{0:<22} *".format(employee.pay))
    print("* {0:<36} *".format(" "))
    print("* Total Pay: £{0:<24} *".format(employee.total_pay))
    print("*"*40)

def pay_slip_generator ():
    print("Pay Slip Generator")
    print(" ")
    employee = input_data()
    print(" ")
    print(" ")
    display_data(employee)
