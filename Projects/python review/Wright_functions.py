# Shawn Wright
# 1/22/18
# Wright_Functions
# this function displays all the functions 
import Wright_grossPay as GP

# main function, will do all of the functions calls
def main():

# function call for number of hours worked
    hours = GP.get_hours()
# function call for hourly rate
    rate = GP.get_rate()
# function call for grossPay
    grossPay = GP.get_grosspay(hours,rates)
# function call for SWT
    SWT = GP.get_SWT(rate,hours)
# function call for FWT
    fwt = GP.get_FWT(rate,hours)
# function call for netPay
    netPay = GP.get_netPay(grossPay,SWT,NWT)
