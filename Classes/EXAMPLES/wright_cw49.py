# Shawn Wright
# 4/9/18
# The file we used in class ( pet)

import pet

def main():
    # local varibles

    pet_name = ""
    pet_type = ""
    pet_age = ""

    # get pet data
    pet_name = input("Enter the name of the pet: ")
    pet_type = input("Enter the type of the pet: ")
    pet_age = int(input("Enter the age of the pet: "))

    # Create an insance of the pet class and assign it to an object
    mypet = pet.Pet(pet_name, pet_type, pet_age)


    # display the datat that was entered
    print("here is the data that you entered")
    print("pet name: ", mypet.get_name())
    print("pet type: ", mypet.get_animal_type())
    print("pet type: ", mypet.get_age())
    













main()
