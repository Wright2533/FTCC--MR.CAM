

print("departments: (1)shoes,(2)clothes,(3)gear,(4)equipment,(5)gifts:")
print(" item names: nike,adidas,jordan:")
num = int(input("Enter How many Departments you want to enter: "))




with open("department items.txt","w") as outfile:
    for count in range(1,num +1):
        dName = input("Enter Department Name:")
        dName = dName.lower()
        dCode = input("Enter your Department Code (1,2,3,4,5):")

        item = input("Enter item:")
        item = item.lower()

        qty = input("Enter Quantity on Hand:")

        price = float(input("Enter Price:"))
        price = price*100
        price = str(int( price))

       

        outfile.write(item.ljust(20) + dName.ljust(10) + dCode.ljust(4) + qty.ljust(3) + price.ljust(4) + "\n" )
