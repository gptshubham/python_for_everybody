# In-built Functions
'''
largest = max('Hello world')
print(largest)
'''

# Custom Functions


# Program: computepay()
def computepay(hour, rate):
    if hour > 40:
        pay = (40 * rate) + ((hour - 40) * (rate * 1.5))
    else:
        pay = hour * rate
    return pay


hrs = input('Enter Hours: ')
rts = input('Enter Rate: ')
try:
    hrf = float(hrs)
    rtf = float(rts)
except:
    print('Error! Please Enter a Numeric Input')
    quit()
pay = computepay(hrf, rtf)
print('Pay', pay)
