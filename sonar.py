#sonar rePrograming
import random
import sys

def makeHeadLine():
    print('     ',end='')
    for i in range(1,6):
        print((' '* 9) + str(i),end='')

def xRagneNum():
    print('    '+'0123456789' * 6);

def makeNewSonarBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            board[x].append('~')
    return board

def makeSonarBoard(theBoard):
    for i in range(15):
        print(str(i).rjust(2,' '),end='  ')
        for j in range(60):
            print(theBoard[j][i],end='')
            if j==59:
                print('',end =' ')
        print(str(i).rjust(2, ' '))

def makeTreasureBox(treasureCnt):
    tempArr=[]
    print()
    for i in range(treasureCnt):
        tempArr.append([random.randint(0,59),random.randint(0,14)])
    return tempArr

def inputData(theBoard,treasureBox,inputCol):
    global checkTreasure
    while True:
        print('please input number (0~59) (0~14)')
        tempData = input()
        inputArr = tempData.split()
        if len(inputArr) == 2 and inputArr[0].isdigit() and inputArr[1].isdigit():
            if int(inputArr[0]) <= 59 and int(inputArr[1]) <= 14:
                inputCol.append([int(inputArr[0]), int(inputArr[1])])
                if searchTargetRange(theBoard,treasureBox,int(inputArr[0]),int(inputArr[1])):
                    checkTreasure =True
                    for x,y in inputCol:
                        searchTargetRange(theBoard,treasureBox,x,y)
                return

def searchTargetRange(theBoard,target,x,y):
    distance = 0
    #비교전 절대적으로 큰 값 입력
    tempDistance  = 100
    #보물의 위치For
    for tx,ty in target:
        if abs(tx-x) > abs(ty-y):
            distance = abs(tx-x)
        else:
            distance = abs(ty-y)
        if distance < tempDistance:
            tempDistance = distance

    if tempDistance == 0:
        ##이것은 보물발견
        target.remove([x,y])
        theBoard[x][y] = '0'
        return True
    else :
        ##보물 미 발견...
        if tempDistance < 10:
            theBoard[x][y] = tempDistance
        else :
            theBoard[x][y] = '0'
        return False



gameCount= 0
treasureBox = makeTreasureBox(3)
theBoard = makeNewSonarBoard()
inputCol = []
print(treasureBox)
while gameCount <14:
    checkTreasure = False
    gameCount +=1
    inputData(theBoard,treasureBox,inputCol)

    print('------------------------------  #'+str(gameCount)+' ------------------------------')
    makeHeadLine()
    print()
    xRagneNum()
    makeSonarBoard(theBoard)
    xRagneNum()
    makeHeadLine()
    if checkTreasure == True:
        print()
        print('sucess find Treasure!!')
    print()