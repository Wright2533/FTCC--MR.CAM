# Shawn Wright
# 1/22/18
# Wright_grossPay
# This program will help calculate gross pay for a user



# main function, will do all of the functions calls
def main():

# function call for number of hours worked
    hours = get_hours()
# function call for hourly rate
    rate = get_rate()
# function call for grossPay
    grossPay = get_grosspay(hours,rates)
# function call for SWT
    SWT = get_SWT(rate,hours)
# function call for FWT
    fwt = get_FWT(rate,hours)
# function call for netPay
    netPay = get_netPay(grossPay,SWT,NWT)

# get input for user
def get_input():
    hours = float(input("Enter the hours worked: "))
    return hours
    rate = float(input("Enter the hourly rate of pay: "))
    return rate

FWT = .02
SWT = .01

# calculation of gross pay and state witholding
def get_grossPay(hours,rates):
    grossPay = hours * rate
    return grossPay

def get_FWT(rate,hours):
    f = grossPay * FWT
    return NWT

def get_SWT(rate,hours):
    s = grossPay * SWT
    return SWT

def get_netPay():
    netPay = grossPay - (f + s)
    return netPay

print(netPay)

# main function call; basically where program starts

if __name__ == "__main__":
    main()
