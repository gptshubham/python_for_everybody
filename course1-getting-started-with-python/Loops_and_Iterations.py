# the most basic example of continue statement
# print out numbers between 1 and 100 that are divisible
# by all 2, 3 and 4 without dividing it by 12 or any multiple of 12

'''
for i in range(1, 101):
    if i % 2 != 0:
        continue
    if i % 3 != 0:
        continue
    if i % 4 == 0:
        print(i)
'''

# Program : 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a Number: ")
    if num == "done":
        break
    try:
        valid_num = int(num)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = valid_num
    if smallest == None:
        smallest = valid_num

    if valid_num < smallest:
        smallest = valid_num

    if valid_num > largest:
        largest = valid_num

print(f'Maximum is {largest}')
print(f'Minimum is {smallest}')
