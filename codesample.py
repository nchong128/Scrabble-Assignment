Board = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]

boardSize = len(Board)

chosenWord = "BOY"
location = "3.5:2:H"
#Give a chosenWord and its location, it will check if the word is allowed to be placed on the board
#at that given location.
def locationCheck(chosenWord,location):
    location = location.split(":")
    
    #Checks if the location is split properly into 3 parts. If it hasn't that means that the colon
    #was not correctly used.
    if len(location) != 3:
        print(": format not followed.")
        return False
    
    #Checks if the d on h:c:d is either H or V
    elif (location[2] != "H") and (location[2] != "V"):
        print("Your direction must be either H or V")
        return False

    #isdigit() is a method that checks if the given string is an integer. This is used
    #to check if the r and c are integers
    elif location[0].isdigit() == False or location[1].isdigit() == False:
        print("Your r and c values must be integers.")
        return False

    return True

locationCheck(chosenWord,location)
