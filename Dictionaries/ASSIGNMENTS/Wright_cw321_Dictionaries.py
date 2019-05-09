#Your Name
#Date

# 1.  How do you create an empty dictionary? Show two different ways
# Show you code below

################
d1 = dict
print(d1)

d2 = {}
print(d2) 
###############

# 2. Which of the following dictionaries are created correctly?
# If they are NOT created correctly write the code to create them correctly
# Then display the information inside inside each dictionary

d = {1:[1, 2], 3:[3, 4]}  #CORRECT
## d = {[1, 2]:1, [3, 4]:3}  #WRONG  d = {:1 (1, 2), :2 (3, 4)} MOVED COLON OVER AND VALUE
## d = {(1, 2):1, (3, 4):3}  #WRONG # d = {1:(1, 2), 2:(3, 4)}   MOVED COLON OVER AND VALUE
## d = {1:"john", 3:"peter"} #CORRECT
## d = {"john":1, "peter":3} #WRONG #d = {1:"john", 3:"peter"}

##d = {:1 (1, 2), :2 (3, 4)} MOVED COLON OVER AND VALUE # number 2
##d = {1:(1, 2), 2:(3, 4)} # number 3
##d = {1:"john", 3:"peter"} # number 4

# Show you code below

#3. Each item in a dictionary has two par ts. What are they called?  VALUE AND KEY


# 4. Suppose a dictionary named students is {"john":3, "peter":2} . What do the following statements do?


##4A. students["susan"] = 5  # SETS A VALUE IF THE KEY IS IN THE DICTIONARY
##
##4B. students["peter"] = 5  # SETS A VALUE IF THE KEY IS IN THE DICTIONARY
##
##4C. students["peter"] += 5 #  SETS A VALUE IF THE KEY OR HIGHER KEY IS IN THE DICTIONARY
##
##4D. del students["peter"]  # DELETES PETER FROME DICTIONARY

# Show your code below be sure to number each and tell me what each code does (brief explanation)

#5. Suppose a dictionary named students is {"john":3, "peter":2} . What do the following statements do? Run the code and tell me waht the code does
##5A. print(len(students)) # SHOWS THE LENGTH OF DICTIONARY
##
##5B. print(students.keys()) # SHOWS ALL KEYS
##
##5C. print(students.values()) # SHOWS ALL VALUES
##
##5D.print(students.items()) # TURNS EVERYTHING INTO A TUPLE

#6. Show the output of the following code: Tell me what it does


##def main():
##    d = {"red":4, "blue":1, "green":14, "yellow":2}
##    print(d["red"])
##    print(list(d.keys()))
##    print(list(d.values()))                 # SHOWS KEYS AND VALUES, TRUE AND FALSE SHOW IF THE VALUES ARE IN THE DICTIONARY
##    print("blue" in d)
##    print("purple" in d)
##    d["blue"] += 10
##
##    print(d["blue"])
     
#main() # Call the main function

##7. Show the output of the following code: Tell me what it does
##def main():
##        d = {}
##        d["susan"] = 50
##    
##        d["jim"] = 45
##    
##        d["joan"] = 54                      # MAKES A DICTIONARY CONTAINING THE VALUES AND KEYS 
##    
##        d["susan"] = 51
##    
##        d["john"] = 53
##    
##        print(len(d))
##     
##        main() # Call the main function

##8.  For a dictionary d , you can use d[key] or d.get(key) to return the value for the key. What are the differences between them?  WHEN YOU SEARCH FOR A RANDOM KEY .GET GIVES YOU NONE. d[key] GIVES A ERROR
##    Give me an example of how eacha re used in code
