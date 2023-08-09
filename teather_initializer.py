from teather_config import roomRow, roomColumn

theather_status = False

def initializer(row, column):

    global theather_status

    print("- "*50)

    if row <= 0 or row > roomRow:
        print("! Linhas inválidas !")
        rowValidation = False
    else:
        rowValidation = True
        print(rowValidation)


    if column <= 0 or column > roomColumn:
        print("! Colunas inválidas !")
        columnValidation = False
    else:
        columnValidation = True
        print(columnValidation)

    print("- "*50)

    if columnValidation == True and rowValidation == True:
        theather_status = True
        return True
    else:
        theather_status = False
        row = 0
        column = 0
        return False