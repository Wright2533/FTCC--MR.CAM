##Shawn Wright
##5/9/19
## Final Exam

class product:  
    def __init__(self, name,price):
        self.__name = name
        self.__price = price


    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price


    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price



class movie(product):
    def __init__(self,name,price,year):
        self.__name = name
        product.__init__(self, year,price)

        self.__year = year

    def set_name(self, name):
        self.__name = name
   

    def set_year(self,year):
        self.__year = year


    def get_year(self):
        return self.__year

    def get_year(self):
        return self.__price

    def get_name(self):
        return self.__name


class book(product):
    def __init__(self,name,price,year,author):
    
        product.__init__(self, author)

        self.__author = author
       
    def set_year(self,author):
        self.__author = author


    def get_year(self):
        return self.__year
   
    
