import datetime
print('Testing')
myDate = datetime.datetime.now()
print(myDate.hour, myDate.minute)
a = 2.5
b = 4
c = 6
d = a + b
myArray = [
    'first',
    'second',
    'third'
]
print(float(1/2), 'convert to ')
if b == c:
    print(d)
else:
    print('Didnt work')

    for x in myArray:
        if x == 'second':
            print(x)
            break

def myFunc(d):
    print(d * 5)

    
myFunc(10)
