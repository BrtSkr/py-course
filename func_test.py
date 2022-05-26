def myFunction1(firstArg, secondArg = 10):
    print(firstArg * secondArg)


def myFunction2(number):
    return number * 2


myFunction1(myFunction2(10))
