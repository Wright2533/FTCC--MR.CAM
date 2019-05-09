#Shawn Wright
#4/4/19
#Hands On Exam Dictionary


# Task 1
print("Shawn Wright")
print("CTI-221")
print("4/4/19")

# Task 2

dcode = dict
print(dcode)

# Task 3

d1 = dict

d1 = {"wrights2533":"[wrights2533@student.faytechcc.edu]","camerona0504":"[cameronaa@student.faytechcc.edu]",
      "averys0414":"[averys0414@student.faytechcc.edu]","mayd0613":"[mayd0613@student.faytechcc.edu]",
      "murraym0926":"[murraym0926@student.faytechcc.edu]","thobet0903":"[thobet0903@student.faytechcc.edu]"}
#print(d1)

# Task 4

d1 = {"wrights2533":"[wrights2533@student.faytechcc.edu]","cameronaa0504":"[camerona@student.faytechcc.edu]",
      "averys0414":"[averys0414@student.faytechcc.edu]","mayd0613":"[mayd0613@student.faytechcc.edu]",
      "murraym0926":"[murraym0926@student.faytechcc.edu]","thobet0903":"[thobet0903@student.faytechcc.edu]"}
print(d1.get("wrights2533","Not found"))

# Task 5
del d1["cameronaa0504"]
d1["camerona0504"] = "camerona@.faytechcc.edu"

print(d1)


# Task 6

print(d1.values())

# Task 7

print(d1.keys())

# Task 8

del d1["murraym0926"]
print(d1)

# Task 9

print(d1)

d1.clear()

print(d1)

# Task 10

d2 = {}
print(d2)







