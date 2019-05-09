NUM_EMPLOYEES = 6

hours = [0] * NUM_EMPLOYEES
# Get each employee's hours worked.
for index in range(NUM_EMPLOYEES):
    print('Enter the hours worked by employee ', \
    index + 1, ': ', sep='', end='')
    hours[index] = float(input())
print(hours)


