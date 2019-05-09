
num = int(input("Enter how many employees do you want to enter: "))
fname = input("Enter your first name:")
lname = input("Enter your last name:")
wname = fname.lower() + lname.lower()



              
with open("employee pay.txt","w") as outfile:
    for count in range(1,num +1):
        title = input("Enter Title (salaried or hourly):")
        title = title.lower()

        payRate = float(input("Enter your pay rate:"))
        
        hoursWorked = float(input("Enter your hours worked:"))
       

        grossPay = int((hoursWorked * payRate))
        payRate = int(payRate * 100)
        hoursWorked = int( hoursWorked  * 100)
        grossPay = int( grossPay  * 100)
 

        payRate = str( payRate)
        hoursWorked = str( hoursWorked)
        grossPay = str( grossPay)
        outfile.write(wname.ljust(20) + title.ljust(10) + payRate.ljust(4) +  hoursWorked.ljust(2) + grossPay.ljust(6) + "\n" )
