# Opening a file
'''
fhandle = open('mbox-short.txt')
# print(fhandle)
'''

# printing lines
'''
fhandle = open('mbox-short.txt')
for line in fhandle:
    print(line)
'''

# counting lines
'''
fhandle = open('mbox-short.txt')
count = 0
for line in fhandle:
    count += 1

print(count)
'''

# Reading the Whole File
'''
fhandle = open('mbox-short.txt')
fcontent = fhandle.read()
print(len(fcontent))
print(fcontent[:20])
'''

# Searching Through a File
'''
fhandle = open('mbox-short.txt')
for line in fhandle:
    if line.startswith('From:'):
        print(line,end='')
'''

# Alternatively
'''
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
'''

# Skipping Lines with continue
'''
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
'''

# Using in to select lines
'''
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
'''


# Prompt for File Name
'''
fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print('File Not Found!',fname)
    quit()
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count += 1
print(count)
fhandle.close()
'''

# Program
'''
fname = input('Enter the file name: ')
fhandle = open(fname)
fcontent = fhandle.read()
fcontent = fcontent.rstrip()
print(fcontent.upper())
'''

# Program
'''
fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print('File Not Found!',fname)
    quit()

count = 0
total = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        data = line[len('X-DSPAM-Confidence:'):]
        data_f = float(data)
        total += data_f

output = total/count
print('Average spam confidence:',output)
'''