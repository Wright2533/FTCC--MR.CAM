#Shawn Wright
#4/30/19
#
#


import Employee
def main():
    
    # local Variables

    name = ''
    number = ''
    shift = ''
    rate = ''

    # Data Attributes
    name = input('Enter the name: ')
    number = int(input('Enter the employee number: '))
    shift = int(input('Enter 1 if day shift and 2 if night shift: '))
    rate = float(input('Enter the hourly rate: '))

    if shift == 1:
        shift = 'Day'
    else:
        shift = 'Night'


    # Create an instance of Employee
    ProductionWorker = Employee.ProductionWorker(name, number, shift, rate)
    print("\n","\n","\n","\n")
    print('Employee Information:')
    print('Name:',ProductionWorker.get_name())
    print('Number:',ProductionWorker.get_number())
    print('shift:',ProductionWorker.get_shift())
    print('Hourly Rate:',ProductionWorker.get_rate())
    
main()

    

    
    
