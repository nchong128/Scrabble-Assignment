import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7  and TILES_USED < len(Tiles):
        myTiles.append(Tiles[TILES_USED])
        TILES_USED += 1


# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)

# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]



scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ")
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
        
if SHUFFLE:
    random.shuffle(Tiles)


myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################
"""
Purpose: This file is to be used for Assignment 1 in FIT1045.
Author: Anonymous
Last modified: 10 April 2018
"""

""" letterCheck(chosenWord)

This function will check if the entered word consists of English letters only (task 1, part 1).
It starts by checking if the letter of chosenWord is not 0, followed by scanning through every 
letter in chosenWord and comparing it against every character in bannedCharacters. 

arguments: chosenWord: This represents the entered word to be scanned through and checked.

returns: Returns False if the word has a length of 0 (i.e. nothing entered) or if the word has
         any letter in it that matches with any character from the bannedCharacters.
         True otherwise.
"""
def letterCheck(chosenWord):
    # Initialisation of the local string variable containing all of the banned characters not
    # allowed in the game
    bannedCharacters = " 12345678\90-=[];',./!@#$%^&*()?_+{}|<>:"
    
    if len(chosenWord) == 0:
        print("You haven't even entered anything!")
        return False

    # Here two for loops is given to compare an individual letter in chosenWord against every
    # individual character in bannedCharacters. If the letter matches a character, it will 
    # return False. After scanning through every character in bannedCharacters, it will move
    # on to the next letter in chosenWords and so on.
    for letter in chosenWord:
        for character in bannedCharacters:
            if letter == character:
                print("Only use English letters!!!")
                return False
    return True

""" dictionaryCheck(chosenWord)

This function will check if the entered word exists in the dictionary.txt file (task 1, part 2).
It does this by scanning through every line in the txt file, checking the scannedWord against
the chosenWord.

arguments: chosenWord: This represents the entered word to be checked against every line in the
                       dictionary.txt file.

returns: Returns True if any scannedWord matches the chosenWord.
         Returns False if the loop reaches the end of the file without any matching.
"""
def dictionaryCheck(chosenWord):
    # Opens the dictionary.txt file in read mode
    dictionaryFile = open("dictionary.txt","r")

    # Runs a for loop to scan through every line in dictionaryFile. The strip() method is
    # used to remove the whitespace for every line, assigning it to scannedWord.
    for line in dictionaryFile:
        scannedWord = line.strip()
        if chosenWord == scannedWord:
            dictionaryFile.close()
            return True
    print("Your word is not found!")
    dictionaryFile.close()
    return False

""" tileCheck(chosenWord)

This function will check if the entered word can be made up from the tiles given (task 1, part
3). It creates a duplicate list of the tiles given in order to not affect the original list of
myTiles. For every letter in the chosenWord, it scans through duplicateTiles and if the letter
matches with any tile in duplicateTiles, the count variable will increment by 1 and the tile 
will be removed from duplicateTiles. After all of the letters in chosenWord are scanned, the
count should match the length of the chosenWord (i.e. every letter in chosenWord should be
found in duplicateTiles and removed)

arguments: chosenWord: The entered word to be checked if it can be made from the tiles given

returns: Returns True if the count matches the length of the chosenWord. False otherwise.

"""
def tileCheck(chosenWord):
    #[:] used to create a duplicate list of myTiles so that duplicateTiles and myTiles do NOT
    #refer to the same object. This allows reusability of the function without affecting
    #the global variable myTiles.
    duplicateTiles = myTiles[:]
    count = 0
    for letter in chosenWord:
        index = 0
        while index < len(duplicateTiles):
            #If the letter matches the tile, then it will be removed from the duplicateTiles
            #to avoid multiple letters in chosenWord to be made up from just one tile.
            if letter == duplicateTiles[index]:
                duplicateTiles.remove(duplicateTiles[index])
                count += 1
                break
            index += 1
    if count != len(chosenWord):
        return False
    else:
        return True

"""totalScore(chosenWord)

This function will total the score for a given word using the function, getScore(letter).
This is used in Task 2 in finding the score of the word.

arguments: chosenWord: The entered word given to check for its score.

returns: Returns the total score of chosenWord.
"""
def totalScore(chosenWord):
    total = 0
    for letter in chosenWord:
        total += getScore(letter)
    return total

#A continuous while loop that will keep running and asking the user for it's input until all
#3 conditions are satisfied
while True:
    chosenWord = input("\nPlease enter a word: ")
    chosenWord = chosenWord.upper()
    #The break command will leave the loop, moving on to find the highest score of the tiles
    if chosenWord == "***":
        print("Better luck next time!")
        break
    if letterCheck(chosenWord) and dictionaryCheck(chosenWord):
        if tileCheck(chosenWord):
            print("Cool, this is a valid word.")
            print("Your score for the word",chosenWord,"is:", totalScore(chosenWord))
            break
        else:
            print("This word cannot be made using the tile")

#To find the highest score, Python will run through every word in dictionary.txt, if the word
#can be made from the tiles and its computed score is higher than the highest score, it will
#be the new highest score.
highestWord = ""
highestScore = 0
dictionaryFile = open("dictionary.txt", "r")

for line in dictionaryFile:
    word = line.strip()
    if tileCheck(word) and (totalScore(word) > highestScore):
        highestWord = word
        highestScore = totalScore(word)
if highestScore == 0:
    print("No word can be made using the tiles")
else:
    print("\nThe word",highestWord,"is the word with the highest score. It's score is",highestScore)



