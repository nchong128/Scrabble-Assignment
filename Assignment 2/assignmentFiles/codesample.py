# REPRESENTS A 5X5 BOARD- DO NOT DELETE
Board = [['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', 'S', 'E','N','T'],['', '', '', '', '','',''],['', '', '', '', '','',''],['', '', '', '', '','','']]
boardSize = len(Board)
wordLocation = ["0","6","V"]
chosenWord = "SENT"
firstMove = False
# REPRESENTS A 5X5 BOARD- DO NOT DELETE

#This function will check if the word will be allowed to be placed into the Board, given a
#syntactically correct location and valid word.
def locationPlaceCheck(chosenWord,location):
    middleOfBoard = len(Board) // 2
    row = int(location[0])
    column = int(location[1])
    horizontalLimit = column + len(chosenWord)
    verticalLimit = row + len(chosenWord)
    lettersPassed = []
    
    #If firstMove is false, it scans through the board using the locations given and place
    #records the number of letters passed into a list. If number of letters passed = 1 and
    #the letter is the letter matching the chosenWord[index] then it is fine. 
    if firstMove == False:
        if location[2] == "H":
            for i in range(column, horizontalLimit):
                    if len(location[row][i]) < 1:
                        lettersPassed.append(Board[row][i])
        
        elif location[2] == "V":
            for i in range(row, verticalLimit):
                    if len(location[i][column]) < 1:
                        lettersPassed.append(Board[i][column])
        
        if len(lettersPassed) < 1:
            print("Invalid move, you must use at least one tile from the Board")
            return False

        for letter in lettersPassed:
            if letter not in chosenWord: #META: Maybe don't use this? #META: Future problem
                #here of the same letters in chosenWord but in different orders
                print("Invalid move, you must use tiles only from the Board")
                return False

    #Checks if word is placed in the middle of the board by ensuring the row and columns
    #are equal to the middle of the board. Applicable only for the first move.
    if firstMove == True and (row != middleOfBoard or column != middleOfBoard):
        print("First move must have the word placed in the middle of the board.")
        return False
    
    #Checks if word is can be placed within the Board's dimension limits
    elif (location[2] == "H" and horizontalLimit > len(Board)) or (location[2] == "V" and verticalLimit > len(Board)):
        print("Word cannot fit on the Board.")
        return False

    return True

print(locationPlaceCheck(chosenWord,wordLocation))