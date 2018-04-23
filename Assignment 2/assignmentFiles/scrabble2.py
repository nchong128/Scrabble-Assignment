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
#Checks if chosenWord is valid and made of English letters
def letterCheck(chosenWord):
    bannedCharacters = " 12345678\90-=[];',./!@#$%^&*()?_+{}|<>:"
    if len(chosenWord) == 0:
        print("You haven't even entered anything!")
        return False
    for letter in chosenWord:
        for character in bannedCharacters:
            if letter == character:
                print("Only use English letters!!!")
                return False
    return True

#Checks if chosenWord is found in the dictionary.txt
def dictionaryCheck(chosenWord):
    dictionaryFile = open("dictionary.txt","r")
    for line in dictionaryFile:
        scannedWord = line.strip()
        if chosenWord == scannedWord:
            dictionaryFile.close()
            return True
    print("Your word is not found!")
    dictionaryFile.close()
    return False

#CHecks if chosenWord can be made from the tiles
def tileCheck(chosenWord):
    duplicateTiles = myTiles[:]
    count = 0
    for letter in chosenWord:
        index = 0
        while index < len(duplicateTiles):
            if letter == duplicateTiles[index]:
                duplicateTiles.remove(duplicateTiles[index])
                count += 1
                break
            index += 1
    if count != len(chosenWord):
        return False
    else:
        return True

#Assuming that the chosenWord and it's location is valid. It will place the word onto the tiles.
def tilePlacer(chosenWord,location):
    pass

#Given a location for the word, it will check if the location is valid.
def locationCheck(location):
    location = location.split(":")
    
    #Checks if the location is split properly into 3 parts. If it hasn't that means that the colon
    #was not correctly used.
    if len(location) != 3:
        print(": format not followed.")
        return False
    
    #Checks if the d on h:c:d is either H or V
    elif location[2] != ("H" or "V"):
        print("Your direction must be either H or V.")
        return False

    #isdigit() is a method that checks if the given string is an integer. This is used
    #to check if the r and c are integers
    elif location[0].isdigit() == False or location[1].isdigit() == False:
        print("Your r and c values must be integers.")
        return False
    
    #Checks if r and c are both between the appropriate range
    elif not(0 <= int(location[1]) < boardSize) or not(0 <= int(location[0]) < boardSize):
        print("Your row and columns are not in range.")
        return False

    return True

while True:
    #Input for chosenWord and location
    chosenWord = input("\nPlease enter a word: ")
    chosenWord = chosenWord.upper()
    wordLocation = input("Enter the location in row:col:direction format: ")
    
    if chosenWord == "***":
        print("Better luck next time!")
        break
    
    elif letterCheck(chosenWord) and dictionaryCheck(chosenWord):
        if tileCheck(chosenWord):
            print("Cool, this is a valid word.")
            break
        else:
            print("This word cannot be made using the tile")