#Shawn Wright
#4/30/19
#


class Employee:  
    def __init__(self, name,number):
        self.__name = name
        self.__number = number


    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number


    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number



class ProductionWorker(Employee):
    def __init__(self, name, number , shift, rate):
    
        Employee.__init__(self, name,number)

        self.__shift = shift
        self.__rate = rate

    def set_shift(self,shift):
        self.__shift = shift

    def set_rate(self,rate):
        self.__rate = rate


    def get_shift(self):
        return self.__shift

    def get_rate(self):
        return self.__rate
    

        

    
        
            
            
    

