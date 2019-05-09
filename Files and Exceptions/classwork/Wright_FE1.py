num = int(input("Enter how many classes do you want to enter: "))
fname = input("Enter your first name:")
lname = input("Enter your last name:")
wname = fname.lower() + lname.lower()


with open("schedule.txt","w") as outfile:
    for count in range(1,num +1):
        className = input("Enter your class name:")
        className = className.lower()
        sTime = input("Enter your class start time:")
        eTime = input("Enter your class end time:")
        days = input("Enter what days of the week your class meets (mtwthf):")
        days = days.lower()
        outfile.write(wname.ljust(20) + className + days.ljust(6) + sTime + eTime + "\n" )
