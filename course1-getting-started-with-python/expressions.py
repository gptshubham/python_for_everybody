# type conversion

# str --> int
'''
sval = '123Hello'
# ival = int(sval)
# ValueError: invalid literal for int() with base 10: '123Hello'
ival = int(sval[0:3])
print(ival)
print(type(ival))

fval = '11.12'
# ival = int(fval)
# ValueError: invalid literal for int() with base 10: '11.12'
ival = int(fval[0:2])
print(ival)
print(type(ival))
'''


# Convert elevator floors
'''
inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor', usf)
'''

# The try Statement
'''
astr = 'Hello bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second',istr)
'''

# Program : calculate total wages to be paid

# without the try statement
'''
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
print(fh, fr)
if fh <= 40:
    pay = fh * fr
else:
    pay = (40 * fr) + ((fh - 40) * (fr * 1.5))
print(pay)
'''

# with the try statement
'''
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter numeric input!')
    quit()

print(fh, fr)
if fh <= 40:
    pay = fh * fr
else:
    pay = (40 * fr) + ((fh - 40) * (fr * 1.5))
print(pay)
'''

# Program :
"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.
"""

score_str = input("Enter Score between the range [0.0,1.0]: ")
# input validation
try:
    score_float = float(score_str)
except:
    print("Error: Please enter numeric input!")
    quit()

# allotment of grade
if 1.0 >= score_float >= 0.0:
    if score_float >= 0.9:
        print('A')
    elif score_float >= 0.8:
        print('B')
    elif score_float >= 0.7:
        print('C')
    elif score_float >= 0.6:
        print('E')
    else:
        print('F')
else:
    print('Error: Score Out of Range!')

