#sonar rePrograming
import random
import sys

def makeHeadLine():
    print('     ',end='')
    for i in range(1,6):
        print((' '* 9) + str(i),end='')

def xRagneNum():
    print()
    print('    '+'0123456789' * 6);

def makeSonarBoard():
    for i in range(15):
        print(str(i).rjust(2,' '),end='  ')
        for j in range(60):
            print('~',end='')
            if j==59:
                print('',end =' ')
        print(str(i).rjust(2, ' '))

def makeTreasureBox(treasureCnt):
    tempArr=[]
    print()
    for i in range(treasureCnt):
        tempArr.append([random.randint(0,59),random.randint(0,14)])
    return tempArr

def inputData():
    #이부분 시작해야함 해당 데이터를 받고 데이터를 배열에바인딩 시켜서 게임을 시작할수있도록.
    data = input()


gameCount= 0
inputColArr = []
treasureBox = makeTreasureBox(3)
inputData()

while gameCount >=14:

    makeHeadLine()
    xRagneNum()
    print()
    makeSonarBoard()
    xRagneNum()
    makeHeadLine()
