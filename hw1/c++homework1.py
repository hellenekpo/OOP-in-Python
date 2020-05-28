

def decryptChar(letter, rotation):
    if (letter >= 'a' and letter <= 'z'):
        letter = chr(ord(letter)-rotation)
        if (letter < 'a'):
            letter = chr(ord(letter)+26)
    return letter

def decryptString(line, rotation):
    newLine = []
    newString = ""
    for i in range(len(line)):
        newLine.append(line[i])
        newLine[i] = decryptChar(newLine[i], rotation)
    return newLine

def makeSentence(charList):
    newWord = ""
    for index in range(len(charList)):
        newWord += charList[index]
    return newWord

def main():
    filestream = open("encrypted.txt", "r")
    rotation = filestream.readline()
    for line in filestream:
        charList = decryptString(line, 5)
        charList.pop()
        print(makeSentence(charList))
    filestream.close()
