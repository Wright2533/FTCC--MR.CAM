#FE2
# Shawn Wright
# 2/26/19
# 

def main ():
  

 

    print( "MENU")
    print( 1, " Report ")


    print( 2, " Average Values : ")

    print( 3, " Exit Program : ")
    
    menuChoice = int(input("Please select the menu option : "))

    if (menuChoice == 1):
    
     with open(" tdsc01titles.txt","w") as outfile:
         h1= " Item ID "
         h2 = " Buyer "
         h3= " Item Name "
         h4= " Price "

         outfile.write( h1.ljust(9) + h2.ljust(20) + h3.ljust(16) + h4 +"\n" )   

         with open(" tdsc01.txt","w") as infile:
             count = 0
             for line in infile:
                 filer = line[0:7]
                 itemID = line[7:10]
                 itemID2 = line[10:13]
                 buyer = line[13:33]
                 buyer = buyer.rstrip(" ")
                 itemName = line[33:48]
                 filer2 = line[48:75]
                 price = line[75:78]
                 price = line[78:80]
                 
                 outfile.write( itemID + "-" + itemID2.ljust(5) + buyer.ljust(20) + itemName.ljust(16) + "$" + price +"\n" )
            
                      
    

    elif (menuChoice == 2):
        print("II")
        with open("Formatted Report.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
               value = int(line)
               count = count + 1
               total = total + value
        ave = total  / count
        print(ave)
   
            
                
    elif (menuChoice == 3):
        print("III")

        quit()

    else:
        print("Error: Restart program and enter a number between 1 and 3." )
  

main() 
