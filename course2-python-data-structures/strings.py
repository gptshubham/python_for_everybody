# indexing vs. slicing
'''
name = 'shubham'

# name[20]
# IndexError: string index out of range

print(name[4:20])
'''

# len() function
'''
name = 'shubham'
print(len(name))
'''

# Looping through string --> my_len() function
'''
def my_len(string):
    count = 0
    for char in string:
        count += 1
    return count


name_length = my_len(name)
print(name_length)
'''

# String Manipulation

# string concatenation

# string methods

# capitalize(), upper(), lower() methods
name = 'shubham'
print(name)

capitalized_name = name.capitalize()
print(capitalized_name)

uppercase_name = name.upper()
print(uppercase_name)

lowercase_name = name.lower()
print(lowercase_name)

# find() method

found_position = name.find('m')
print(found_position)

found_position = name.find('k')
print(found_position)

# replace method
greet = 'Hello shubham'
updated_greet = greet.replace('shubham','kumar')
print(updated_greet)
print(greet)

updated_greet = greet.replace('h','X')
print(updated_greet)

# stripping whitespaces --> strip(), lstrip(), rstrip() methods
# strip()
greet = '   Hello shubham        '
print(greet)
greet = greet.strip()
print(greet)
# lstrip()
greet = '   Hello shubham        '
greet = greet.lstrip()
print(greet + 'kumar')
# rstrip()
greet = '   Hello shubham        '
greet = greet.rstrip()
print(greet + 'kumar')

# prefixes
name = 'shubham'
print(name.startswith('s'))
print(name.startswith('S'))

# Program : Parsing and Extracting
data = 'form stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
at_position = data.find('@')
print(at_position)

space_position = data.find(' ',at_position)
print(space_position)

host = data[at_position + 1 : space_position]
print(host)

