import re # regex


# https://stackoverflow.com/questions/11556810/count-matching-brackets-in-python-string


def countBracket(string, c=0):
    left_bracket = string.find("{")
    if left_bracket > -1:
        string = string[left_bracket + 1:]
        right_bracket = string.find("}")
        if right_bracket > -1:
            if string[:right_bracket].find("{") == -1:
                c += 1
            string = string[right_bracket + 1:]
        return countBracket(string, c)
    else:
        return c


def readingFromFile():
    starterFile = open('lab03/game.txt','r+')
    gameContent = starterFile.read()

    arrayOfUserInput = re.findall('\{.*?\}',gameContent)
    answerFile = open('lab03/answer.txt','w+')
    # answerFile.write(gameContent)
    answerContent = answerFile.read()

    for item in arrayOfUserInput:
        userInput= input( f"enter {item}")
       # item1= item.translate({ord('{'):None, ord('}'):None})
      
       # gameContent.format(userInput)
        #print(22222222,gameContent.format(userInput))
        gameContent = gameContent.replace(item, userInput)
        print(11111,gameContent)
    answerFile.write(gameContent)
    





readingFromFile()
# answerFile1 = open('lab03/answer.txt','w+')
# answerContent1 = answerFile1.read()
# print(answerContent1)






    





