NUMBERS = 20

hours = [0] * NUMBERS
# Get each employee's hours worked.
for index in range(NUMBERS):
    print('Enter a series of 20 Numbers ', \
    index + 1, ': ', sep='', end='')
    hours[index] = float(input())
print(hours)

print("The lowest number in the list is ")
hours = min(hours)

print("The highest number in the list is ")
hours = max(hours)
