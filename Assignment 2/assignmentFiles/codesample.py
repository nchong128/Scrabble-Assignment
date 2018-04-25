# REPRESENTS A 5X5 BOARD- DO NOT DELETE
Board = [['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','','']]
boardSize = len(Board)
firstMove = False
wordLocation = ["3","3","V"]

# REPRESENTS A 5X5 BOARD- DO NOT DELETE

#This function will place the VALID word into Board using the location (r:c:d) given
#META: Will need adjustment to changign everything after the first tile
def tilePlacer(chosenWord,location):
    row = int(location[0])
    column = int(location[1])
    WordIndex = 0

    if firstMove == True:
        pass

    #Dealing with where the word is to be placed horizontally
    elif location[2] == "H":
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

tilePlacer("TONE",wordLocation)
print(Board)