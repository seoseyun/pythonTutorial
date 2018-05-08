#balge game start

import random

def getTargetArr(numCount):
    tempArr = []
    while True:
        randomNum = random.randint(0,9)
        if not randomNum in tempArr:
            tempArr.append(randomNum)
        if len(tempArr) >= numCount:
            return tempArr

def startDisplay(numCount):
    print('I am thinking of a ' + str(numCount) + '-digit number.Tryto guess what it is.')
    print('Here are somclues:')
    print('when i say:    That means:')
    print('     Pico:     One digitis correnct but in the wrong position.')
    print('     Fermi:    One digit is correct andin theright position.')
    print('     Bagels:   No digit is correct.')

def findTargetNum(target,input,arrKey):
    if target[arrKey] == input[arrKey]:
        return 'Pico'
    elif input[arrKey] in target:
        return 'Fermi'
    else:
        return 'NONE'
def convertInt(num):
    return int(num)

replay = True
numLong = 6
while replay:

    target = getTargetArr(numLong)
    print(target)
    startDisplay(numLong)

    gameCount = 0
    while True:
        gameCount += 1
        print('Guess #'+str(gameCount))
        while True:
            print('please six latter number')
            temp = input()
            if len(temp) == numLong:
                break
        A = list(temp)
        for x in range(len(A)):
            A[x] = int(A[x])
        print(A)
        if A == target:
            print('Nice! good game')
            print('Do you want replay? (yes or no)')
            answer = input()
            if answer == 'no':
                replay=False
            break
        for i in range(0,numLong):
            print(findTargetNum(target,A,i),end=' ')
        print()