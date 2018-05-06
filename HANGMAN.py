#HANGMANGAME

import random

HANGMANGRAPIC = ['''
    +----+
    |    |
         |
         |
         |
         |
==============''','''
    +----+
    |    |
    0    |
         |
         |
         |
==============''','''
    +----+
    |    |
    0    |
    |    |
         |
         |
==============''','''
    +----+
    |    |
    0    |
    |-   |
         |
         |
==============''','''
    +----+
    |    |
    0    |
   -|-   |
         |
         |
==============''','''
    +----+
    |    |
    0    |
   -|-   |
   /     |
         |
==============''','''
    +----+
    |    |
    0    |
   -|-   |
   / /   |
         |
==============''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getWord(wordList):
    randint = random.randint(0,len(wordList)-1)
    return wordList[randint]

def getGuess(aleadyInputGuess):
    while True:
        print()
        print('please input guess latter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please single latter')
        elif guess in aleadyInputGuess:
            print('this latter is aleady latter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter latter')
        else:
            return guess

def displayBoard(graphic,sucessGuess,missGuess,resultWord):
    print('now missword count :'+str(len(missGuess)))
    print()

    print(graphic[len(missGuess)])

    print('miss latter : ',end=' ')
    for latter in missGuess:
        print(latter,end=' ')
    print()

    blanks = '_' * len(resultWord)
    

    print('sucess latter:' , end=' ')
    for i in range(len(resultWord)):
        if resultWord[i] in sucessGuess:
            blanks = blanks[:i] + resultWord[i]+ blanks[i+1:]

    for latter in blanks:
        print(latter,end=' ')

def requestReplay():
    checkReplay=input()
    if checkReplay.lower() == 'yes':
        return True
    else:
        return False


while True:
    missLatter= []
    sucessGuess = []
    aleadyLatter = []
    resultWord = getWord(words)
    print(resultWord)

    while len(missLatter) != 6:
        displayBoard(HANGMANGRAPIC,sucessGuess,missLatter,resultWord)
        inputlatter = getGuess(aleadyLatter)
        aleadyLatter.append(inputlatter)

        if inputlatter in resultWord:
            sucessGuess.append(inputlatter)
        else:
            missLatter.append(inputlatter)

        sucessCheck = True

        #완료체크하는거 더 생각해봅시다.
        for i in range(len(resultWord)):
            if resultWord[i] not in sucessGuess:
                sucessCheck = False
        
        if sucessCheck == True:
            print('YOU WIN!')
            print('TO BE CONTINUE? (YES OR NO)')
            break
    
    if not requestReplay():
        break
print('END Game')
