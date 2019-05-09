#Shawn Wright
#5/9/19
#
#


import product
def main():
    
    # local Variables

    name = ''
    price = ''
    year = ''
    

    # Data Attributes
    name = input('Enter the name of product: ')
    price = int(input('Enter the price of the product: '))
    
   

    


    # Create an instance of Employee
    movie = product.movie(name,price,year)
    print("\n","\n","------------------","\n","\n")
    print('Product Information:')
    print('Name:',movie.get_name())
    print('Price:',movie.get_price())
    
    
main()

    

    
    
