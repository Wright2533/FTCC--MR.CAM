# programming Exercise 11-3

class Person:
    def __init__(self, name,adress, phone_number):
        self.__name = name
        self.__adress = adress
        self.__phone_number = phone_number


    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    
     def get_phone_number(self):
        return self.__phone_number


class Customer(Person)

   
   
    

