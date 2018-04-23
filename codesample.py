Board = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]

boardSize = len(Board)

location = "1011:111:H"

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

print(locationCheck(location))
