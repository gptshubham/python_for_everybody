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
inp = input('Europe floor? ')
usf = int(inp) + 1
print('US floor', usf)

