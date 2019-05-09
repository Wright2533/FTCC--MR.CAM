#FE2

def main ():
   menu()

def menu ():
    
    print( "MENU")
    print( 1, " Create text file : ")


    print( 2, " Average Values : ")

    print( 3, " Total Values : ")

    print( 4 , " File Exception : ")

    print( 5, " Value Error Exception : ")

    print( 6, " Exit Program : ")
    
    userNumber = int(input("Please select one number from the list above : "))

    if userNumber == 1:
    
        with open("FE2.txt","r") as outfile:
         count = int(input("enter a number"))
         for count in range(1,count +1):
                 number = int(input("enter a number:"))    
                 outfile.write(str(number) + "\n")

           
    

    elif userNumber == 2:
        print("II")
        with open("FE2.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
               value = int(line)
               count = count + 1
               total = total + value
        ave = total  / count
        print(ave)
        
    elif userNumber == 3:
        print("III")
        with open("FE2.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
               value = int(line)
               count = count + 1
               total = total + value
            print(total)
            
    elif userNumber == 4:
        print("IV")
        with open("FE2.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
               value = int(line)
               count = count + 1
               total = total + value
               print(total)
               except IOError:
                   print("file not found or corrupt")
               
    elif userNumber == 5:
        print("V")
        with open("FE2.txt","r") as infile:
            total = 0
            count = 0
            for line in infile:
               value = int(line)
               count = count + 1
               total = total + value
               except ValueError:
                   print("Bad data is found on Line ", count + 1, sep = " ")

        
    elif userNumber == 6:
        print("VI")

        quit()

    else:
        print("Error: Restart program and enter a number between 1 and 6." )

    main()


main()



 
