# Project1: Connect4

def draw_field(field):
    for row in range(12):
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(14):
                if column % 2 == 1:
                    practical_column = int(column / 2)
                    if column != 10:
                        print(field[practical_column][practical_row], end="")
                    else:
                        print(field[practical_column][practical_row], end="")
                else:
                    print("|", end="")
            print("| ")
        else:
            print("---------------")


Player = 1

CurrentField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]]

draw_field(CurrentField)

while True:
    print("Players turn: ", Player)
    MoveRow = -1
    MoveColumn = int(input("Please enter the column\n"))
    MoveColumn -= 1
    if Player == 1:
        if CurrentField[MoveColumn][MoveRow] == " ":
            CurrentField[MoveColumn][MoveRow] = "X"
            draw_field(CurrentField)
            Player = 2
        else:
            MoveRow -= 1
            if CurrentField[MoveColumn][MoveRow] == " ":
                CurrentField[MoveColumn][MoveRow] = "X"
                draw_field(CurrentField)
                Player = 2
            else:
                MoveRow -= 1
                if CurrentField[MoveColumn][MoveRow] == " ":
                    CurrentField[MoveColumn][MoveRow] = "X"
                    draw_field(CurrentField)
                    Player = 2
                else:
                    MoveRow -= 1
                    if CurrentField[MoveColumn][MoveRow] == " ":
                        CurrentField[MoveColumn][MoveRow] = "X"
                        draw_field(CurrentField)
                        Player = 2
                    else:
                        MoveRow -= 1
                        if CurrentField[MoveColumn][MoveRow] == " ":
                            CurrentField[MoveColumn][MoveRow] = "X"
                            draw_field(CurrentField)
                            Player = 2
                        else:
                            MoveRow -= 1
                            if CurrentField[MoveColumn][MoveRow] == " ":
                                CurrentField[MoveColumn][MoveRow] = "X"
                                draw_field(CurrentField)
                                Player = 2
                            else:
                                Player = 1
    else:
        if CurrentField[MoveColumn][MoveRow] == " ":
            CurrentField[MoveColumn][MoveRow] = "O"
            draw_field(CurrentField)
            Player = 1
        else:
            MoveRow -= 1
            if CurrentField[MoveColumn][MoveRow] == " ":
                CurrentField[MoveColumn][MoveRow] = "O"
                draw_field(CurrentField)
                Player = 1
            else:
                MoveRow -= 1
                if CurrentField[MoveColumn][MoveRow] == " ":
                    CurrentField[MoveColumn][MoveRow] = "O"
                    draw_field(CurrentField)
                    Player = 1
                else:
                    MoveRow -= 1
                    if CurrentField[MoveColumn][MoveRow] == " ":
                        CurrentField[MoveColumn][MoveRow] = "O"
                        draw_field(CurrentField)
                        Player = 1
                    else:
                        MoveRow -= 1
                        if CurrentField[MoveColumn][MoveRow] == " ":
                            CurrentField[MoveColumn][MoveRow] = "O"
                            draw_field(CurrentField)
                            Player = 1
                        else:
                            MoveRow -= 1
                            if CurrentField[MoveColumn][MoveRow] == " ":
                                CurrentField[MoveColumn][MoveRow] = "O"
                                draw_field(CurrentField)
                                Player = 1
                            else:
                                Player = 2
