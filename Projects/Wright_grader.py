# Shawn Wright
# 1/22/19
# Wright_grade_grader
# This program will call the other functions
import Wright_grade_functions as functions

# main function that will do all of the functions calls
def main():
# function call and return # of grades to enter
    num = functions.get_input()
# function call and return average
    average = functions.get_average(num)
# function call and return letter grade
    letter_grade = functions.get_letter_grade(average)
# function call to print letter grade
    functions.display_grade(average,letter_grade)

main()
