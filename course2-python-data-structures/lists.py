# # List Methods
# x = []
# print(type(x))

# list_methods = dir(x)
# print(list_methods)
# # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# Alternatively
# print(dir(list))

# # append()
# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# stuff.append('cookie')
# print(stuff)

# # sort()
# friends = ['joseph', 'glenn', 'sally']
# friends.sort()
# print(friends)

# # Built-in Functions and Lists
# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums)/len(nums))

# Lists and Strings

# # split() function
# abc = 'with three words'
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])
# for w in stuff:
#     print(w)
#
# line = 'a lot                       of spaces'
# etc = line.split()
# print(etc)
#
# line = 'first;second;third'
# thing = line.split(';')
# print(thing)

# # parsing from mail data
# fname = input('Enter the file name: ')
# fhandle = open(fname)
# for line in fhandle:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words)
# fhandle.close()

# # The Double Split Pattern
# fname = input('Enter the file name: ')
# fhandle = open(fname)
# for line in fhandle:
#     line = line.rstrip()
#     if not line.startswith('From '): continue
#     words = line.split()
#     pieces = words[1].split('@')
#     print(pieces[1])
# fhandle.close()

# # Program : romeo.txt
# fname = input('Enter the file name: ')
# fhandle = open(fname)
# list_of_words = []
# for line in fhandle:
#     line = line.rstrip()
#     words = line.split()
#     for word in words:
#         if word in list_of_words:
#             continue
#         list_of_words.append(word)
# list_of_words.sort()
# print(list_of_words)

# Program : mbox-short.txt : address of the person who sent the msg

# fname = input('Enter the file name: ')
# fhandle = open(fname)
# count = 0
# for line in fhandle:
#     line = line.rstrip()
#     if line.startswith('From '):
#         pieces = line.split()
#         print(pieces[1])
#         count += 1
# print(f'There were {count} lines in the file with From as the first word')
