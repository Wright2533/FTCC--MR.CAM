#CW_27
# Demo how to throw exceptions
try:
   num = int(input("Enter how many numbers you want to get from the user: "))

    with open("numbers.txt", "w") as outfile:
       for count in range(1,num +1):
           number = int(input("enter a number:"))
           outfile.write(str(number) + "\n")

except ValueError:
  print("Incorrect entry. Entries should be integers:")

try:
    with open("numbers.txt","r") as infile:
        total = 0
        count = 0
        for line in infile:
           value = int(line)
           count = count + 1
           total = total + value
        ave = total  / count
        badData =  print(total)
        print(ave)
        
except ValueError:
    print("Bad data is found on Line ", count + 1, sep = " ")
    
except IOError:
   print("file not found or corrupt")



   
