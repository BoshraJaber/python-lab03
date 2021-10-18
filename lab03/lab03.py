import re # regex

def readingFromFile():
    starterFile = open('lab03/game.txt','r+')
    gameContent = starterFile.read()

    arrayOfUserInput = re.findall('\{.*?\}',gameContent)
    answerFile = open('lab03/answer.txt','w+')
    answerContent = answerFile.read()

    for item in arrayOfUserInput:
        userInput= input( f"enter {item}")
       # item1= item.translate({ord('{'):None, ord('}'):None})
        gameContent = gameContent.replace(item, userInput)
        print(11111,gameContent)
    answerFile.write(gameContent)
    
readingFromFile()





    





