import random


def getNumber(number):
    #print(number)
    isAnswered = False
    answer = int(input('enter a number '))
    while(isAnswered == False):
        if(answer == number):
            print("You're correct!!")
            isAnswered = True
        else:
            print('Wrong answer')
            answer = int(input('enter a number '))


getNumber(random.randint(1, 100))
