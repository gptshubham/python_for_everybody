# # Empty Dictionary
# d = dict()
# print(type(d))
#
# d1 = {}
# print(type(d1))

# # Counting Pattern
# counts = dict()
# line = input('Enter a line of text: ')
# '''
# The general pattern to count the words in a line of text is to split the line into words,
# then loop through the words and use a dictionary to track the count of each word independently.
# '''
#
# words = line.split()
#
# print("Words: ",words)
#
# print('counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts',counts)

# # Definite Loops and Dictionaries
# counts = {'chuck': 1, 'fred': 42, 'jan': 100}
# for key in counts:
#     print(key, counts[key])

# # Retrieving Keys and Values of a Dictionary
# counts = {'chuck': 1, 'fred': 42, 'jan': 100}
#
# print(list(counts))
#
# print(counts.keys())
# print(list(counts.keys()))
#
# print(counts.values())
# print(list(counts.values()))
#
# print(counts.items())
# print(list(counts.items()))

# # Two Iteration Values
# counts = {'chuck': 1, 'fred': 42, 'jan': 100}
# for key, value in counts.items():
#     print(key, value)

# Program : word count from a text file and word with max count
'''
fname = input('Enter the file name: ')
fhandle = open(fname)
counts = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# print(len(list(counts)))
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
'''

# Program : sender who sent maximum mail messages along with number of messages
fname = input('Enter the file name: ')
fhandle = open(fname)
mail_count = dict()
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        pieces = line.split()
        # print(pieces)
        for piece in pieces:
            if '@' in piece:
                mail_count[piece] = mail_count.get(piece, 0) + 1
# print(mail_count)

big_mail_id = ''
big_count = -1
for mail_id, count in mail_count.items():
    # print(mail_id, count)
    if count > big_count:
        big_count = count
        big_mail_id = mail_id
print(big_mail_id, big_count)
