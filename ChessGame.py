from termcolor import colored

board = []
for i in range(64):
    board.append(0)
xlabels = ["A", "B", "C", "D", "E", "F", "G", "H"]

pieces = {
    "\u265A": "WhiteKing",
    "\u265B": "WhiteQueen",
    "\u265D": "WhiteBishop",
    "\u265E": "WhiteKnight",
    "\u265C": "WhiteRook",
    "\u265F": "WhitePawn",
    "\u2654": "BlackKing",
    "\u2655": "BlackQueen",
    "\u2656": "BlackRook",
    "\u2657": "BlackBishop",
    "\u2658": "BlackKnight",
    "\u2659": "BlackPawn",
}

whitePromotion = {
    "WhiteQueen": "\u265B",
    "WhiteBishop": "\u265D",
    "WhiteKnight": "\u265E",
    "WhiteRook": "\u265C",
}
blackPromotion = {
    "BlackQueen": "\u2655",
    "BlackRook": "\u2656",
    "BlackBishop": "\u2657",
    "BlackKnight": "\u2658",
}
letters = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}


def printBoard():
    print("-----------------------------------")
    for i in range(63, -1, -1):
        if (i + 1) % 8 == 0:
            print(colored("{:.0f} :".format((i + 1) / 8), "blue"), end="\t")
        print(board[i], end="\t")
        if i % 8 == 0 and i != 0:
            print()
    print()
    print("-----------------------------------")
    print("  ", end="\t")
    for x in xlabels:
        print(colored(x, "blue"), end="\t")
    print()


def checkforPromotion(unicode, player, end_position):
    if player == "White":
        if (55 < end_position < 64):
            print("Your Pawn has been Promoted !!")
            for x in whitePromotion.keys():
                print(x, end="\t")
            print()
            piece = input("Please select one of the following pieces to promote to: ")
            while piece not in whitePromotion.keys():
                piece = input("Please select one of the following pieces to promote to: ")
            unicode = whitePromotion.get(piece)
            return unicode
        else:
            return unicode
    else:
        if (-1 < end_position < 8):
            print("Your Pawn has been Promoted !!")
            for x in blackPromotion.keys():
                print(x, end="\t")
            print()
            piece = input("Please select one of the following pieces to promote to: ")
            while piece not in blackPromotion.keys():
                piece = input("Please select one of the following pieces to promote to: ")
            unicode = blackPromotion.get(piece)
            return unicode
        else:
            return unicode


def pawn(player, end_position, start_position):
    if player == "White":
        if (start_position > 7) and (start_position < 16):
            if (((end_position == start_position + 8 and type(board[start_position + 8]) == type(8)) or (
                    end_position == start_position + 16 and type(board[start_position + 8]) == type(8) and type(
                board[start_position + 16]) == type(8)))):
                return True
            else:
                return False
        else:
            if end_position == start_position + 8 and type(board[start_position + 8]) == type(8):
                return True
            elif (end_position == start_position + 7) or (end_position == start_position + 9):
                val = board[end_position]
                unicode = pieces.get(val, "")
                if unicode.startswith("Black"):
                    return True
                else:
                    return False
            else:
                return False
    else:
        if 47 < start_position < 56:
            if (((end_position == start_position - 8 and type(board[start_position - 8]) == type(8)) or (
                    end_position == start_position - 16 and type(board[start_position - 8]) == type(8) and type(
                board[start_position - 16]) == type(8)))):
                return True
            else:
                return False
        else:
            if end_position == start_position - 8 and type(board[start_position - 8]) == type(8):
                return True
            elif (end_position == start_position - 7) or (end_position == start_position - 9):
                val = board[end_position]
                unicode = pieces.get(val, "")
                if unicode.startswith("White"):
                    return True
            else:
                return False


def queen(player, end_position, start_position):
    rightUp = [(start_position + (i * 7)) for i in range(1, (start_position % 8) + 1)]
    leftup = [(start_position + (i * 9)) for i in range(1, (8 - (start_position % 8 + 1)) + 1)]
    rightdown = [(start_position - (i * 9)) for i in range(1, (start_position % 8) + 1)]
    leftdown = [(start_position - (i * 7)) for i in range(1, (8 - (start_position % 8 + 1)) + 1)]
    right = [(start_position - i) for i in range(1, (start_position % 8 + 1))]
    left = [(start_position + i) for i in range(1, 8 - (start_position % 8 + 1) + 1)]
    up = [(start_position + i * 8) for i in range(1, ((64 - start_position) // 8 + 1))]
    down = [(start_position - i * 8) for i in range(1, (8 - ((64 - start_position) // 8)))]
    if end_position in rightUp:
        for i in range((start_position + 7), end_position, 7):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in leftup:
        for i in range((start_position + 9), end_position, 9):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in rightdown:
        for i in range((start_position - 9), end_position, -9):
            if (type(board[i]) != type(8)):
                return False
        return checkKill(player, end_position)
    elif end_position in leftdown:
        for i in range((start_position - 7), end_position, -7):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in right:
        for i in range((start_position + 1), end_position, 1):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in left:
        for i in range((start_position - 1), end_position, -1):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in up:
        for i in range((start_position + 8), end_position, +8):
            if type(board[i]) != type(8):
                return False
        return (checkKill(player, end_position))
    elif end_position in down:
        for i in range((start_position - 8), end_position, -8):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    else:
        return False


def bishop(player, end_position, start_position):
    rightUp = [(start_position + (i * 7)) for i in range(1, (start_position % 8) + 1)]
    leftup = [(start_position + (i * 9)) for i in range(1, (8 - (start_position % 8 + 1)) + 1)]
    rightdown = [(start_position - (i * 9)) for i in range(1, (start_position % 8) + 1)]
    leftdown = [(start_position - (i * 7)) for i in range(1, (8 - (start_position % 8 + 1)) + 1)]
    if end_position in rightUp:
        for i in range((start_position + 7), end_position, 7):
            if (type(board[i]) != type(8)):
                return False
        return checkKill(player, end_position)
    elif end_position in leftup:
        for i in range((start_position + 9), end_position, 9):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in rightdown:
        for i in range((start_position - 9), end_position, -9):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in leftdown:
        for i in range((start_position - 7), end_position, -7):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    else:
        return False


def rook(player, end_position, start_position):
    right = [(start_position - i) for i in range(1, (start_position % 8 + 1))]
    left = [(start_position + i) for i in range(1, 8 - (start_position % 8 + 1) + 1)]
    up = [(start_position + i * 8) for i in range(1, ((64 - start_position) // 8 + 1))]
    down = [(start_position - i * 8) for i in range(1, (8 - ((64 - start_position) // 8)))]
    if end_position in right:
        for i in range((start_position + 1), end_position, 1):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in left:
        for i in range((start_position - 1), end_position, -1):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in up:
        for i in range((start_position + 8), end_position, +8):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    elif end_position in down:
        for i in range((start_position - 8), end_position, -8):
            if type(board[i]) != type(8):
                return False
        return checkKill(player, end_position)
    else:
        return False


def knight(player, end_position, start_position):
    # move two squares horizontally or vertically, then can move a further one space vertically or horizontally
    # can jump over pieces
    valid_move = False
    val = board[end_position]

    if (end_position == (start_position - 2) + 8) or (end_position == (start_position - 2) - 8):
        valid_move = True
    elif (end_position == (start_position - 1) + 16) or (end_position == (start_position - 1) - 16):
        valid_move = True
    elif (end_position == (start_position + 1) - 16) or (end_position == (start_position + 1) + 16):
        valid_move = True
    elif (end_position == (start_position + 2) - 8) or (end_position == (start_position + 2) + 8):
        valid_move = True
    unicode = pieces.get(val, "")
    if valid_move and not unicode.startswith(player):
        return True
    else:
        return False


def king(player, end_position, start_position):
    validmoves = []
    if start_position % 8 == 0:
        pass
    else:
        right = start_position - 1
        validmoves.append(right)
    if (start_position + 1) % 8 == 0:
        pass
    else:
        left = start_position + 1
        validmoves.append(left)
    if start_position + 8 > 63:
        pass
    else:
        up = start_position + 8
        validmoves.append(up)
    if start_position - 8 < 0:
        pass
    else:
        down = start_position - 8
        validmoves.append(down)
    if ((start_position + 1) % 8 == 0) or (start_position + 8 > 63):
        pass
    else:
        upleft = start_position + 9
        validmoves.append(upleft)
    if (start_position + 8 > 63) or (start_position % 8 == 0):
        pass
    else:
        upright = start_position + 7
        validmoves.append(upright)
    if ((start_position + 1) % 8 == 0) or (start_position - 8 < 0):
        pass
    else:
        downleft = start_position - 7
        validmoves.append(downleft)
    if (start_position - 8 < 0) or (start_position % 8 == 0):
        pass
    else:
        downright = start_position - 9
        validmoves.append(downright)
    if end_position in validmoves:
        return checkKill(player, end_position)
    else:
        return False


def checkKill(player, end_position):
    val = board[end_position]
    unicode = pieces.get(val, "")
    if unicode.startswith(player):
        return False
    else:
        return True


for i in range(8):
    # col
    for j in range(8):
        if (i == 0 and j == 0) or (i == 0 and j == 7):
            board[j] = "\u265C"
        elif (i == 0 and j == 1) or (i == 0 and j == 6):
            board[j] = "\u265E"
        elif (i == 0 and j == 2) or (i == 0 and j == 5):
            board[j] = "\u265D"
        elif i == 0 and j == 3:
            board[j] = "\u265A"
        elif i == 0 and j == 4:
            board[j] = "\u265B"
        elif i == 1:
            # 8-15
            board[j + 8] = "\u265F"
        elif i == 6:
            board[i * 8 + j] = "\u2659"
        elif (i == 7 and j == 0) or (i == 7 and j == 7):
            board[i * 8 + j] = "\u2656"
        elif i == 7 and j == 1 or i == 7 and j == 6:
            board[i * 8 + j] = "\u2658"
        elif i == 7 and j == 2 or i == 7 and j == 5:
            board[i * 8 + j] = "\u2657"
        elif i == 7 and j == 3:
            board[i * 8 + j] = "\u2654"
        elif i == 7 and j == 4:
            board[i * 8 + j] = "\u2655"
printBoard()
won = False
turn = 0
while not won:
    if turn % 2 == 0:
        # white
        print("White's Turn")
        valid = False
        while not valid:
            startPosition = input("Select a piece to move (e.g.A2): ").lower()
            # A*R + (8-A)
            letter = startPosition[0:1]
            if not startPosition[1:].isdigit():
                continue
            number = int(startPosition[1:])
            letterValue = int(letters.get(letter, -1))
            if letterValue == -1 or (number > 8) or (number < 1):
                print("Please Enter a valid space on the board White....")
                continue
            start_index = int(8 * number) - int(letterValue)
            unicode = board[start_index]
            print(unicode)
            piece = pieces.get(unicode, "")
            print(colored(piece, "green"))
            if piece.startswith("W"):
                endPosition = input("Select a position to move to (e.g.A4): ").lower()
                letter = endPosition[0:1]
                number = int(endPosition[1:])
                # RESTRICT NUMBER TO 1-8
                # AND GIVE DEFAULT VALUE OF LETTER DICTIONARY AND CHECK IF IT'S NOT THAT
                letterValue = int(letters.get(letter, -1))
                end_index = int(8 * number) - int(letterValue)
                if letterValue == -1 or (number > 8) or (number < 1):
                    print("Please Enter a valid space on the board White....")
                else:
                    print(end_index)
                    if piece == "WhitePawn":
                        valid = pawn("White", end_index, start_index)
                        if valid == True:
                            unicode = checkforPromotion(unicode, "White", end_index)
                    if piece == "WhiteBishop":
                        valid = bishop("White", end_index, start_index)
                    if piece == "WhiteRook":
                        valid = rook("White", end_index, start_index)
                    if piece == "WhiteKnight":
                        valid = knight("White", end_index, start_index)
                    if piece == "WhiteQueen":
                        valid = queen("White", end_index, start_index)
                    if piece == "WhiteKing":
                        valid = king("White", end_index, start_index)
                    if valid:
                        print("You can make this move!!")
                        board[start_index] = 0
                        board[end_index] = unicode
                        printBoard()
                        turn = turn + 1
                    else:
                        print("This move is INVALID")
                        print("Please Select again white")
            else:
                print(colored("You have NOT Selected a Valid piece, please enter again...", "red"))

    else:
        print("Black's Turn")
        valid = False
        while not valid:
            startPosition = input("Select a piece to move (e.g.A2): ").lower()
            # A*R + (8-A)
            letter = startPosition[0:1]
            number = int(startPosition[1:])
            letterValue = int(letters.get(letter, -1))
            if letterValue == -1 or (number > 8) or (number < 1):
                print("Please Enter a valid space on the board Black....")
                continue
            start_index = int(8 * number) - int(letterValue)
            unicode = board[start_index]
            print(unicode)
            piece = pieces.get(unicode, "")
            print(colored(piece, "green"))

            if piece.startswith("B"):
                endPosition = input("Select a position to move to (e.g.A4): ").lower()
                letter = endPosition[0:1]
                number = int(endPosition[1:])
                # RESTRICT NUMBER TO 1-8
                # AND GIVE DEFAULT VALUE OF LETTER DICTIONARY AND CHECK IF IT'S NOT THAT
                letterValue = int(letters.get(letter, -1))
                end_index = int(8 * number) - int(letterValue)
                if letterValue == -1 or (number > 8) or (number < 1):
                    print("Please Enter a valid space on the board Black....")
                else:
                    print(end_index)
                    if piece == "BlackPawn":
                        valid = pawn("Black", end_index, start_index)
                        if valid == True:
                            unicode = checkforPromotion(unicode, "Black", end_index)
                    if piece == "BlackBishop":
                        valid = bishop("Black", end_index, start_index)
                    if piece == "BlackRook":
                        valid = rook("Black", end_index, start_index)
                    if piece == "BlackKnight":
                        valid = knight("Black", end_index, start_index)
                    if piece == "BlackQueen":
                        valid = queen("Black", end_index, start_index)
                    if piece == "BlackKing":
                        valid = king("Black", end_index, start_index)
                    if valid:
                        # CHECK KILL HERE
                        print("You can make this move!!")
                        board[start_index] = 0
                        board[end_index] = unicode
                        printBoard()
                        turn = turn + 1
                    else:
                        print("This move is INVALID")
                        print("Please Select again black")
            else:
                print(colored("You have NOT Selected a Valid piece, please enter again...", "red"))