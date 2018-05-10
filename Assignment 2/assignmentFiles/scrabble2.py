from sys import stdin
import math
import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
CELL_WIDTH = 3 # cell width of the scrabble board
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7 and TILES_USED < len(Tiles):
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

# initialize n x n Board with empty strings
def initializeBoard(n):
    Board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("")
        Board.append(row)

    return Board

# put character t before and after the string s such that the total length
# of the string s is CELL_WIDTH.
def getString(s,t):
    global CELL_WIDTH
    s = str(s)
    rem = CELL_WIDTH - len(s)
    rem = rem//2
    s = t*rem + s
    rem = CELL_WIDTH - len(s)
    s = s + t*rem
    return s

# print the Board on screen
def printBoard(Board):
    global CELL_WIDTH
    print("\nBoard:")
    spaces = CELL_WIDTH*" "
    board_str =  "  |" + "|".join(getString(item," ") for item in range(len(Board)))  +"|"
    line1 = "--|" + "|".join(getString("","-") for item in range(len(Board)))  +"|"

 
    print(board_str)
    print(line1)
    
    for i in range(len(Board)):
        row = str(i) + " "*(2-len(str(i))) +"|"
        for j in range(len(Board)):
            row += getString(Board[i][j]," ") + "|"
        print(row)
        print(line1)
        
    print()

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


validBoardSize = False
while not validBoardSize:
    BOARD_SIZE = input("Enter board size (a number between 5 to 15): ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE >= 5 and BOARD_SIZE <= 15:
            validBoardSize = True
        else:
            print("Your number is not within the range.\n")
    else:
        print("Are you a little tipsy? I asked you to enter a number.\n")


Board = initializeBoard(BOARD_SIZE)
printBoard(Board)

myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################
"""
Purpose: This file is to be used in Assignment 2 for FIT1045.
Author: Anonymous
Last modified: 10 May 2018
"""

# Global variables declared to be used throughout the code
firstMove = True
totalScore = 0
MIDDLE_OF_BOARD = BOARD_SIZE // 2

""" isIn(target, collection)

This function will check if the target is present in the collection by scanning through
every item in the collection and comparing it against the target.

arguments: target: a string/list/number to be compared with.
           collection: a string/list/number to be searched through.

returns: Returns True if the target is in the collection. False otherwise.
"""
def isIn(target, collection):
    for item in collection:
        if target == item:
            return True
    return False

""" letterCheck(word)

This function will check if the argument consists of only alphabets (defined below)

arguments: word: a string to be checked for alphabets

returns: Returns False if any character in the string is not in the Alphabet list OR
         the word has 0 length. True otherwise.
"""
def letterCheck(word):
    Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',  'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    if len(word) == 0:
        print("You haven't even entered anything!")
        return False
    for letter in word:
        if isIn(letter.upper(), Alphabets) == False:
            return False
    return True

""" dictionaryCheck(word)

This function will check if the entered word exists in the dictionary.txt file by scanning
through every line in the txt file, checking the scannedWord against the word.

arguments: word: This represents the entered word to be checked against every line in the
                 dictionary.txt file.

returns: Returns True if any scannedWord matches the word.
         Returns False if the loop reaches the end of the file without any matching.
"""
def dictionaryCheck(word):
    dictionaryFile = open("dictionary.txt","r")
    for line in dictionaryFile:
        scannedWord = line.strip()
        if word == scannedWord:
            dictionaryFile.close()
            return True
    dictionaryFile.close()
    return False

""" tileCheck(word, tiles)

Checks if a given word can be made from the tiles.

arguments: word: A string to be checked through against the tiles.
           tiles: A list of characters that the word argument can be made of.

returns: False if any letter in the word is not present in the tileCopy. True otherwise.
"""
def tileCheck(word, tiles):
    # Copy method used to create a duplicate of the 'tiles' list without any references
    # to it. Allows for reusability of the function without affecting the global variable
    tileCopy = tiles.copy()
    for letter in word:
        if isIn(letter, tileCopy) == False:
            return False
        else:
            tileCopy.remove(letter)
    return True

""" currentTileCheck(word,location)

This function will find all of the tiles already present on the Board, transforming them into
a suitable table.

arguments: word: A string given to be checked for its length, used as part of the upper bound
                 of the range() when searching.
           location: The location (in r:c:d format) to check for letters.

returns: A table, lettersPassed, containing lists (commonly known as letterPairs in this code)
         of letters found (at index 1) and its location (at index 0)
"""
def currentTileCheck(word,location):
    row = int(location[0])
    column = int(location[1])
    lettersPassed = []
    index = 0
    
    # The endpoint for where the function should be stopped searching is defined depending on
    # if the search was horizontal or vertical.
    if location[2] == "H":
        endPoint = column + len(word)
        for columnNumber in range(column, endPoint):
            if len(Board[row][columnNumber]) == 1:
                letterPair = [index,Board[row][columnNumber]]
                lettersPassed.append(letterPair)
            index += 1
    
    elif location[2] == "V":
        endPoint = row + len(word)
        for rowNumber in range(row, endPoint):
            if len(Board[rowNumber][column]) == 1:
                letterPair = [index,Board[rowNumber][column]]
                lettersPassed.append(letterPair)
            index += 1

    return lettersPassed

""" moveScore(word,location)

Computes the score for a given word at a specified location. The location needs
to be specified in order to avoid counting the score of letters already on the 
Board.

arguments: word: The word which the score will be counted for.
           location: The location of where the word is to be placed (in r:c:d format).

returns: The total score as a number.
"""
def moveScore(word,location):
    total = 0
    # lettersPassed is a TABLE containing LISTS of letters and its location index for a
    # given location and word. See currentTileCheck documentation for more info.
    lettersPassed = currentTileCheck(word,location)

    for letterIndex in range(len(word)):
        letterInBoard = False
        # letter variable created in a similar format to a list in lettersPassed. Both in
        # ["letter's index", "letter"] format.
        letter = [letterIndex, word[letterIndex]]
        if isIn(letter, lettersPassed):
            letterInBoard = True
        if letterInBoard == False:
            total += getScore(letter[1])

    return total

""" wordIsValid(word,location)

Puts a given word and location through all 3 criterias for a given word. If any condition
is not met, it will print the reason why.

argument: word: The word to check for validity.
          location: The location to check for validity.

returns: False if any of the conditions are not met. True otherwise.
"""
def wordIsValid(word,location):
    if letterCheck(word) == False:
        print("Only use English letters!!")
        return False

    elif dictionaryCheck(word) == False:
        print("Your word doesn't exist in the dictionary!!!")
        return False

    # duplicateTiles created to allow reusability (see above for copy method explanation).
    # Appends all of the letters already on the Board at the given location to duplicateTiles.
    duplicateTiles = myTiles.copy()
    for letterPair in currentTileCheck(word,location):
        duplicateTiles.append(letterPair[1])
    
    if tileCheck(word,duplicateTiles) == False:
        print("This word cannot be made using the tiles!!")
        return False

    return True

""" locationSyntaxCheck(location)

Function will check if the location fits multiple syntax conditions.

arguments: location: The string to be checked through if it follows all of the conditions

returns: False if any of the conditions are not met. True otherwise.
"""
def locationSyntaxCheck(location):
    # If the location is not split into 3 parts (not having a length of 3), then the r:c:d
    # format was improperly used/not used.
    if len(location) != 3:
        return False

    #Checks if the d in h:c:d is either H or V
    elif location[2] != "H" and location[2] != "V":
        return False

    # isdigit() is a method that checks if the given string is an integer. This is used
    # to check if the r and c are integers.
    elif location[0].isdigit() == False or location[1].isdigit() == False:
        return False
    
    # Checks if r and c are both between the appropriate range.
    elif not(0 <= int(location[1]) < BOARD_SIZE) or not(0 <= int(location[0]) < BOARD_SIZE):
        return False
    
    return True

""" locationPlaceCheck(word,location)

Function will check if the word is allowed to be placed on a Board, given a valid word and 
a syntactically correct location.

arguments: word: The word to be checked if it may be placed on the Board.
           location: A syntactically correct location (i.e. Assuming that it satisfies locationSyntaxCheck)

returns: A list containing a Boolean showing whether it may be placed on the Board or not (True if it can be
         placed, False otherwise) and a reason for why the location is False (only if it is False).
"""
def locationPlaceCheck(word,location):
    row = int(location[0])
    column = int(location[1])
    
    horizontalLimit = column + len(word)
    verticalLimit = row + len(word)
    lettersPassed = []
    
    # Checks if the word can be placed within the Board's dimension limits
    if (location[2] == "H" and horizontalLimit > BOARD_SIZE) or (location[2] == "V" and verticalLimit > BOARD_SIZE):
        reason = "Invalid move! The word cannot fit on the Board."
        return [False,reason]
    
    # Checks if the word is placed in the middle of the board by ensuring the row and column are equal to the middle
    # of the board. Applicable only for the first move.
    if firstMove == True and (row != MIDDLE_OF_BOARD or column != MIDDLE_OF_BOARD):
        reason = "Invalid move! The location in the first move must be " + str(MIDDLE_OF_BOARD) + ":" + str(MIDDLE_OF_BOARD) + ":H or " + str(MIDDLE_OF_BOARD) + ":" + str(MIDDLE_OF_BOARD) + ":V."
        return [False,reason]
    
    if firstMove == False:
        lettersPassed = currentTileCheck(word,location)
        
        # Checks if the word overlaps against any tiles already on the Board (i.e. If the word uses at least one tile.)
        if len(lettersPassed) < 1:
            reason = "Invalid move! You must use at least one tile from the Board."
            return [False,reason]

        # Also checks if the word actually matches with the overlapped tiles by checking if the letter location is the
        # same for both the word and the tiles on the Board.
        for letterPair in lettersPassed:
            if (letterPair[1] != word[letterPair[0]]):
                reason = "Invalid move! The word must match the tile on the board at the correct location."
                return [False,reason]
    
    return [True]

""" locationIsValid(word,location)

Function will check if both functions, locationSyntaxCheck and locationPlaceCheck, are satisfied.

arguments: word: The word ot be passed into both functions for checking.
           location: The location to be passed into both functions for checking.

returns: Returns False if either of the functions are false. True otherwise.

"""
def locationIsValid(word,location):
    if locationSyntaxCheck(location) == False:
        print("Invalid move!!!")
        return False
    elif locationPlaceCheck(word,location)[0] == False:
        #Prints the reason for failure, see locationPlaceCheck documentation
        print(locationPlaceCheck(word,location)[1])
        return False
    return True

""" tilePlacer(word,location)

Function will place the valid word into the list of lists, Board.

arguments: word: The word to be placed.
           location: The location (in r:c:d format) for the word to be placed on the Board

returns: No returns
"""
def tilePlacer(word,location):
    row = int(location[0])
    column = int(location[1])
    WordIndex = 0

    #Dealing with where the word is to be placed horizontally
    if location[2] == "H":
        endPoint = column + len(word)
        for columnNumber in range(column, endPoint):
            Board[row][columnNumber] = word[WordIndex]
            WordIndex += 1

    #Dealing with where the word is to be placed vertically
    elif location[2] == "V":
        endPoint = row + len(word)
        for rowNumber in range(row, endPoint):
            Board[rowNumber][column] = word[WordIndex]
            WordIndex += 1

""" tileRemover(word,location)

Removes the letters from primaryList, which contains the letters already on the Board at
a location previously defined (see bottom of code). This allows for the pre-existing tiles
on the Board to be acknowledged and removed. Letters that are not in primaryList are removed
from myTiles.

arguments: word: The word to be scanned through and have all of its letters removed from 
                 primaryList OR myTiles
    
returns: Nothing.
"""
def tileRemover(word):
    for letter in word:
        if isIn(letter,primaryList):
            primaryList.remove(letter)
        elif isIn(letter,myTiles):
            myTiles.remove(letter)

""" maximumMoveScore()

Function will find the maximum score for each move. Further documentation is in efficient.pdf.
It is advised to read efficient.pdf for an overview before reading this function.

arguments: None

returns: None
"""
def maximumMoveScore():
    maxScore = 0
    maxWord = ""
    letterPool = []
    wordPool = []

    # Makes letterPool by adding myTiles' letters and letters already in the Board
    for tile in myTiles:
        letterPool.append(tile)

    for row in Board:
        for letter in row:
            if len(letter) > 0:
                letterPool.append(letter) 
    
    # Creates the wordPool by appending words from dictionary.txt, making sure they
    # satisfy certain conditions
    dictionaryFile = open("dictionary.txt","r")
    
    for line in dictionaryFile:
        scannedWord = line.strip()
        validWordFlag = True

        if tileCheck(scannedWord,letterPool) == False:
            validWordFlag = False
        elif len(scannedWord) > BOARD_SIZE:
            validWordFlag = False
        
        if validWordFlag:
            wordPool.append(scannedWord)
    dictionaryFile.close()

    # rowsFilled represents the indexes of all the rows that contain a letter in it
    # columnsFilled represents the indexes of all the columns that contain a letter in it
    rowsFilled = []
    columnsFilled = []

    #Finds the rows and columns that are filled with a letter, ignoring duplicates.
    for primaryIndex in range(BOARD_SIZE):
        for secondaryIndex in range(BOARD_SIZE):
            if len(Board[primaryIndex][secondaryIndex]) > 0 and not isIn(primaryIndex, rowsFilled):
                rowsFilled.append(primaryIndex)
            
            if len(Board[secondaryIndex][primaryIndex]) > 0 and not isIn(primaryIndex, columnsFilled):
                columnsFilled.append(primaryIndex)

    # Scans through every possible word in the wordPool
    for possibleWord in wordPool:
        # Finds the best possible move for the first move. The possible location can only start in the middle
        # of the Board, with either "H" or "V", which the code accounts for.
        if firstMove:
            possibleLocation = [str(MIDDLE_OF_BOARD),str(MIDDLE_OF_BOARD),"H"]
            # Ensures that the word can be made up of the tiles first before checking if the location is valid
            # and if the move's score is higher than the max score.
            if tileCheck(possibleWord, myTiles):
                if locationPlaceCheck(possibleWord,possibleLocation)[0] and (moveScore(possibleWord,possibleLocation) > maxScore):
                    # Proceeds to update the max word and max score with the max position
                    maxWord = possibleWord
                    maxScore = moveScore(possibleWord,possibleLocation)
                    maxPosition = possibleLocation
                else:
                    possibleLocation[2] = "V"
                    if locationPlaceCheck(possibleWord,possibleLocation)[0] and (moveScore(possibleWord,possibleLocation) > maxScore):
                        maxWord = possibleWord
                        maxScore = moveScore(possibleWord,possibleLocation)
                        maxPosition = possibleLocation
        
        # Deals with finding the best possible move AFTER the first move
        else:
            # Scans through all of the columns/rows, generalised under "secondaryNumber" as long as the word
            # can fit in the Board
            for secondaryNumber in range(BOARD_SIZE - len(possibleWord) + 1):
                # Varies the row number for words to be placed horizontally
                for rowNumber in rowsFilled:
                    possibleLocation = [str(rowNumber),str(secondaryNumber),"H"]
                    
                    # Creates duplicateTiles from myTiles, adding tiles already on the Board, to be used in tileCheck
                    duplicateTiles = myTiles.copy()
                    for letterPair in currentTileCheck(possibleWord,possibleLocation):
                        duplicateTiles.append(letterPair[1])
                    
                    if tileCheck(possibleWord,duplicateTiles):
                        if locationPlaceCheck(possibleWord,possibleLocation)[0] and (moveScore(possibleWord,possibleLocation) > maxScore):
                            maxWord = possibleWord
                            maxScore = moveScore(possibleWord,possibleLocation)
                            maxPosition = possibleLocation

                # Varies the column number for words to be placed vertically
                for columnNumber in columnsFilled:
                    possibleLocation = [str(secondaryNumber),str(columnNumber),"V"]
                    
                    duplicateTiles = myTiles.copy()
                    for letterPair in currentTileCheck(possibleWord,possibleLocation):
                        duplicateTiles.append(letterPair[1])
                    
                    if tileCheck(possibleWord,duplicateTiles):
                        if locationPlaceCheck(possibleWord,possibleLocation)[0] and (moveScore(possibleWord,possibleLocation) > maxScore):
                            maxWord = possibleWord
                            maxScore = moveScore(possibleWord,possibleLocation)
                            maxPosition = possibleLocation

    if moveScore(chosenWord,wordLocation) == maxScore:
        print("Your move was the best move! Well done!")
    
    print("Maximum possible score in this move was " + str(maxScore) + " with word " + str(maxWord) + " at " + str(maxPosition[0]) + ":" + str(maxPosition[1]) + ":" + str(maxPosition[2]))


# A continuous while loop that will keep allowing the user to input words and locations to be placed
# on the Board until the word is "***"
while True:
    #Input for chosenWord and location
    chosenWord = input("\nPlease enter a word: ")
    chosenWord = chosenWord.upper()

    # break command here is the only way to exit the while loop here
    if chosenWord == "***":
        print("Better luck next time!!!")
        break

    wordLocation = input("Enter the location in row:col:direction format: ")
    wordLocation = wordLocation.split(":")    
    
    # Checks if the word and location is valid. Note that two if statements are used
    # Due to some assumptions from wordIsValid relying on if locationIsValid is true
    if locationIsValid(chosenWord, wordLocation):
        if wordIsValid(chosenWord,wordLocation):
            maximumMoveScore()

            if firstMove:
                firstMove = False
            
            #Finding the move's score and adding it to the total score
            totalScore += moveScore(chosenWord,wordLocation)
            print('Your score in this move: ' + str(moveScore(chosenWord,wordLocation)))
            print('Your total score is: ' + str(totalScore))
            
            # Creates a primaryList containing every letter already on the Board
            # at a given location. primaryList is used in the tileRemover function
            primaryList = []
            for letterPair in currentTileCheck(chosenWord,wordLocation):
                primaryList.append(letterPair[1])

            # Remaining functions called to advance to the next move
            tilePlacer(chosenWord,wordLocation)
            printBoard(Board)
            tileRemover(chosenWord)
            getTiles(myTiles)
            printTiles(myTiles)