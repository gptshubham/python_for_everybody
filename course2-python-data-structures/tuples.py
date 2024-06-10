# # Tuples and Assignment
# (x, y) = (4, 'fred')
# print(x)
# print(y)
#
# num, name = (4, 'fred')
# print(num)
# print(name)

# # Optional Parenthesis
# ages = 99, 98, 97, 96, 95
# print(ages)
# print(type(ages))
#
# for age in ages:
#     print(age, end=' ')
# print()

# # Tuples and Dictionaries
# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k, v) in d.items():
#     print(k, v)
# tups = d.items()
# print(tups)

# # Sorting Lists of Tuples
# d = {'a': 10, 'c': 22, 'b': 1}
# print(d.items())
# print(sorted(d.items()))
#
# for k, v in sorted(d.items()):
#     print(k, v)

# # Sorting by Values instead of Keys
# d = {'a': 10, 'c': 22, 'b': 1}
# temp_list = list()
# for k, v in d.items():
#     temp_list.append((v, k))
# print(temp_list)
#
# temp_list = sorted(temp_list, reverse=True)
# print(temp_list)

# Program : Top 10 Most Common Words
'''
fname = input('Enter the file name: ')
fhandle = open(fname)
word_dictionary = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1
# print(word_dictionary)

temp_list = list()
for k, v in word_dictionary.items():
    temp_list.append((v, k))
# print(temp_list)

temp_list = sorted(temp_list, reverse=True)
# print(temp_list[:10])

for v, k in temp_list[:10]:
    print(k, v)

# Alternatively , using list comprehension
fname = input('Enter the file name: ')
fhandle = open(fname)
word_dictionary = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1

new_temp_list = sorted([(v, k) for k, v in word_dictionary.items()],reverse=True)
for v, k in new_temp_list[:10]:
    print(k, v)
'''

# L = [1, 2, 3, 4]
# T = (5, 6, 7, 8)
# print(L.index(2))
# print(T.index(6))

# L.sort(reverse=True)
# print(L)

# Program : read through the file and figure out the distribution by hour
fname = input('Enter the file name: ')
fhandle = open(fname)
hour_distribution = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        pieces = line.split()
        # print(pieces)
        for piece in pieces:
            if ':' in piece:
                time_stamps = piece.split(':')
                # print(time_stamps)
                hour_distribution[time_stamps[0]] = hour_distribution.get(time_stamps[0], 0) + 1

# print(hour_distribution)
sorted_hour_distribution = sorted(hour_distribution.items())
# print(sorted_hour_distribution)
for k, v in sorted_hour_distribution:
    print(k, v)