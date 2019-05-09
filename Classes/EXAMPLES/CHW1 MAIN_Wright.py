# Shawn Wright
# 4/9/18
# The file we used in class ( pet)

import CHW1_Wright as car

def main():
    # local varibles

    

    car_year_model = ""
    car_make = ""


    # Get data

    car_year_model = input("Enter the Year Model of the Car: ")
    car_make = input("Enter the Make of the Car: ")


    mycar=car.Car(car_year_model ,car_make)

    for i in range (5):
        mycar.accelerate()
        print(mycar.get_speed())

    for i in range (5):
        mycar.deaccelerate()
        print(mycar.get_speed())    

    


    
    
    
    
    

    









main()
