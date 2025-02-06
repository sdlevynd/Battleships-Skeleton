# Battleship Skeleton Program

import random


def GetRowColumn():
    print()

    valid = False
    while not valid:
        try:
            Row = int(input("Please enter row: "))
            if (Row < 0 or Row > 9):
                print ("Out of bounds of the board, please enter again")
            else:
                valid = True
        except ValueError:
            print("Incorrect data type")


    valid = False
    while not valid:
        try:
            Column = int(input("Please enter Column: "))
            if (Column < 0 or Column > 9):
                print ("Out of bounds of the board, please enter again")
            else:
                valid = True
        except ValueError:
            print("Incorrect data type")

    print()
    return Row, Column


def MakePlayerMove(Board, Ships):
    Row, Column = GetRowColumn()
    if Board[Row][Column] == "m" or Board[Row][Column] == "h":
        print("Sorry, you have already shot at the square (" + str(Row) + "," + str(Column) + "). Please try again.")
    elif Board[Row][Column] == "-":
        print("Sorry, (" + str(Row) + "," + str(Column) + ") is a miss.")
        Board[Row][Column] = "m"
    else:
        print("Hit at (" + str(Row) + "," + str(Column) + ").")
        Board[Row][Column] = "h"


def SetUpBoard(RowNumber = 10, ColumnNumber = 10):
    Board = []
    for Row in range(RowNumber):
        BoardRow = []
        for Column in range(ColumnNumber):
            BoardRow.append("-")
        Board.append(BoardRow)
    return Board


def LoadGame(Filename, Board):
    BoardFile = open(Filename, "r")
    for Row in range(10):
        Line = BoardFile.readline()
        for Column in range(10):
            Board[Row][Column] = Line[Column]
    BoardFile.close()


def PlaceRandomShips(Board, Ships):
    for Ship in Ships:
        Valid = False
        while not Valid:
            Row = random.randint(0, 9)
            Column = random.randint(0, 9)
            HorV = random.randint(0, 1)
            if HorV == 0:
                Orientation = "v"
            else:
                Orientation = "h"
            Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
        print("Computer placing the " + Ship[0])
        PlaceShip(Board, Ship, Row, Column, Orientation)


def PlaceShip(Board, Ship, Row, Column, Orientation):
    if Orientation == "v":
        for Scan in range(Ship[1]):
            Board[Row + Scan][Column] = Ship[0][0]
    elif Orientation == "h":
        for Scan in range(Ship[1]):
            Board[Row][Column + Scan] = Ship[0][0]


def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
    if Orientation == "v" and Row + Ship[1] > len(Board[0]):
        return False
    elif Orientation == "h" and Column + Ship[1] > len(Board):
        return False
    else:
        if Orientation == "v":
            for Scan in range(Ship[1]):
                if Board[Row + Scan][Column] != "-":
                    return False
        elif Orientation == "h":
            for Scan in range(Ship[1]):
                if Board[Row][Column + Scan] != "-":
                    return False
    return True


def CheckWin(Board):
    for Row in range(10):
        for Column in range(10):
            if Board[Row][Column] in ["A", "B", "S", "D", "P"]:
                return False
    return True


def PrintBoard(Board):
    print()
    print("The board looks like this: ")
    print()
    print(" ", end="")
    columnSize = 20
    rowSize = 20
    for Column in range(10):
        print(" " + str(Column) + "  ", end="")
    print()
    for Row in range(10):
        print(str(Row) + " ", end="")
        for Column in range(10):
            if Board[Row][Column] == "-":
                print(" ", end="")
            elif Board[Row][Column] in ["A", "B", "S", "D", "P"]:
                print(" ", end="")
            else:
                print(Board[Row][Column], end="")
            if Column != 9:
                print(" | ", end="")
        print()


def DisplayMenu():
    print("MAIN MENU")
    print()
    print("1. Start new game")
    print("2. Load training game")
    print("9. Quit")
    print()


def GetMainMenuChoice():
    print("Please enter your choice: ", end="")
    choiceEntered = False
    while not choiceEntered:
        try:
            Choice = int(input("Please enter your choice: "))
            choiceEntered = True
        except :
            print("try again...")        

    print()
    return Choice


def PlayGame(Board, Ships):
    GameWon = False
    while not GameWon:
        PrintBoard(Board)
        MakePlayerMove(Board, Ships)
        GameWon = CheckWin(Board)
        if GameWon:
            print("All ships sunk!")
            print()


if __name__ == "__main__":
    TRAININGGAME = "Training.txt"
    MenuOption = 0
    while not MenuOption == 9:
        
        Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
        DisplayMenu()
        MenuOption = GetMainMenuChoice()
        if MenuOption == 1:
            row = int(input("enter number of rows"))
            col = int(input("enter number of columns"))
            Board = SetUpBoard(row,col)
            PlaceRandomShips(Board, Ships)
            PlayGame(Board, Ships)
        if MenuOption == 2:
            Board = SetUpBoard()
            LoadGame(TRAININGGAME, Board)
            PlayGame(Board, Ships)
