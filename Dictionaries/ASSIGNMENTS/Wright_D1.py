### Wright_D1
#3/26/19
#


# Encrypt 
def main():
    menu()

# print menu
print('\nMenu')
print('1. Encrypt file')
print('2. Decrypt file')
print('3. Exit Program\n')
choice = int(input('Please enter your choice: '))
#get choice

if (choice == 1):
    
        with open ("text.txt","r") as infile:
            r = ''
            text = infile.read()
            d1 = { "A" : "1", "a" : "2", "B" : "3", "b" : "4","C" : "5","c" : "6","D" : "7","d" : "8",
                   "E" : "9", "e" : "!", "F" : "@", "f" : "#","G" : "$","g" : "%","H" : "^","h" : "&",
                   "I" : "Z", "i" : "z", "J" : "Y", "j" : "y","K" : "X","k" : "x","L" : "W","l" : "w",
                   "M" : "V", "m" : "v", "N" : "U", "n" : "u","O" : "T","o" : "t","P" : "S","p" : "s",
                   "Q" : "R", "q" : "r", "R" : "Q", "r" : "q","S" : "P","s" : "p","T" : "O","t" : "o",
                   "U" : "N", "u" : "n", "V" : "M", "v" : "m","W" : "L","w" : "l","X" : "K","x" : "k",
                   "Y" : "J", "y" : "j", "Z" : "I", "z" : "i","0" : "9","1" : "8","2" : "7","3" : "6",
                   "4" : "5", "5" : "4", "6" : "3", "7" : "2","8" : "1","9" : "0","," : "*","." : "+",
                   "-" : "=", "'" : ".", " " : ",", "\n" : "<"}

        for ch in text:
           r = r + d1[ch]
        print(r)
        with open('encrypt.txt','w') as outfile:
            outfile.write(r)

               
# Decrypt
elif (choice == 2):
   
        with open ("encrypt.txt","r") as infile:
            r = ''
            text = infile.read()
            d2 = { "1" : "A", "2" : "a", "3" : "B", "4" : "b","5" : "C","6" : "c","7" : "D","8" : "d",
                   "9" : "E", "!" : "e", "@" : "F", "#" : "f","$" : "G","%" : "g","^" : "H","&" : "h",
                   "Z" : "I", "z" : "i", "Y" : "J", "y" : "j","X" : "K","x" : "k","W" : "L","w" : "l",
                   "V" : "M", "v" : "m", "U" : "N", "u" : "n","T" : "O","t" : "o","S" : "P","s" : "p",
                   "R" : "Q", "r" : "q", "Q" : "R", "q" : "r","P" : "S","p" : "s","O" : "T","o" : "t",
                   "N" : "U", "n" : "u", "M" : "V", "m" : "v","L" : "W","l" : "w","K" : "X","k" : "x",
                   "J" : "Y", "j" : "y", "I" : "Z", "i" : "z","9" : "0","8" : "1","7" : "2","6" : "3",
                   "5" : "4", "4" : "5", "3" : "6", "2" : "7","1" : "8","0" : "9","*" : ",","+" : ".",
                   "=" : "-", "." : "'", ",": " ", "<" : "\n"}


        for ch in text:
           r = r + d2[ch]
        print(r)
        with open('decrypt.txt','w') as outfile:
            outfile.write(r)

elif (choice ==3):
    quit()
           
##           
           
           
           
           
    

    
 
