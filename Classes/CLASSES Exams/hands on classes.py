# Hands on Exam Classes
# write a class called HumanBeing in a file called human.py
# Create the default constructor, mutators and accessors
# do the following
# write the import statement

##Shawn Wright
##5/9/19
##


import human 

def main():
    # Local variables
    name = ""
    sex = ""
    age = 0
    
    # Get human data.
    name = input('Enter your name: ')
    sex = input('Enter whether you are female or male: ')
    age = int(input('Enter your age: '))

    # Create an instance of HumanBeing class and 
    # assign to an object
    myhuman=human.HumanBeing(name, sex, age)

    # Display the data that was entered.
    # correct the "?" marks
    print ("---------------------------------------")
    print ('Here is the data that you entered: ')
    print ('My Name: ', myhuman.get_name())
    print ('Sex: ', myhuman.get_sex())
    print ('My Age: ', myhuman.get_age())

# Call the main function.
main()

