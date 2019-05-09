'''
Shawn Wright
5/9/19
Wright_human
'''
class HumanBeing:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def set_name(self, name):
        self.__name = name
    def set_sex(self, sex):
        self.__sex = sex
    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    def get_sex(self):
        return self.__sex
    def get_age(self):
        return self.__age
    
        
