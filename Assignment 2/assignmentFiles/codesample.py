# REPRESENTS A 5X5 BOARD- DO NOT DELETE
Board = [['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','','']]
boardSize = len(Board)
firstMove = False
wordLocation = ["3","3","V"]

# REPRESENTS A 5X5 BOARD- DO NOT DELETE

#This function will check if the word will be allowed to be placed into the Board, given a
#syntactically correct location and valid word.
def locationPlaceCheck(chosenWord,location):
    middleOfBoard = len(Board) // 2
    
    row = int(location[0])
    column = int(location[1])

    horizontalLimit = row + len(chosenWord)
    verticalLimit = column + len(chosenWord)
    
    #Checks if word is placed in the middle of the board by ensuring the row and columns
    #are equal to the middle of the board.
    if location[0] != middleOfBoard or location[1] != middleOfBoard:
        print("First move must have the word placed in the middle of the board.")
        return False
    
    #Checks if word is can be placed within the Board's dimension limits
    elif (location[2] == "H" and horizontalLimit > len(Board)) or (location[2] == "V" and verticalLimit > len(Board)):
        print("Word cannot fit on the Board.")
        return False

    return True

#This function will place the VALID word into Board using the location (r:c:d) given
#META: Will need adjustment to changign everything after the first tile
def tilePlacer(chosenWord,location):
    row = int(location[0])
    column = int(location[1])
    WordIndex = 0

    #Dealing with where the word is to be placed horizontally
    if location[2] == "H":
        endPoint = column + len(chosenWord)
        for i in range(column, endPoint):
            Board[row][i] = chosenWord[WordIndex]
            WordIndex += 1

    #Dealing with where the word is to be placed vertically
    elif location[2] == "V": #META: May need changing to just else: ?
        endPoint = row + len(chosenWord)
        for i in range(row, endPoint):
            Board[i][column] = chosenWord[WordIndex]
            WordIndex += 1

print(locationPlaceCheck("TONE",wordLocation))
