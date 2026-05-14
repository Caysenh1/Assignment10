def check_position(pos):
    first = 'abcdefgh'
    second = '12345678'

    if pos[0] in first and pos[1] in second and len(pos) == 2:
        return True
    else:
        return False

while True:
    user = input("Enter a legal chess coordinate: ")
    if check_position(user) == True:
        break

def knight_moves(pos):
    
    first = 'abcdefgh'
    second = '12345678'
    numPos = (first.index(pos[0]) + 1, int(pos[1]))

    
    board = []
    for i in range(1,9):
        for j in range(1,9):
            board.append((i,j))

    
    alphaBoard = []
    for letter in first:
        for number in second:
            alphaBoard.append(f"{letter}{number}")

    
    boardPairings = dict(zip(board, alphaBoard))

    
    allMoves = []
    for i in range(1,8):
        
        allMoves.append((numPos[0] + i, numPos[1] + 2*i))

        
        allMoves.append((numPos[0] + 2*i, numPos[1] + i))

        
        allMoves.append((numPos[0] + i, numPos[1] - 2*i))

        
        allMoves.append((numPos[0] + 2*i, numPos[1] - i))
        

        allMoves.append((numPos[0] - i, numPos[1] + 2*i))

        
        allMoves.append((numPos[0] - 2*i, numPos[1] + i))

        
        allMoves.append((numPos[0] - i, numPos[1] - 2*i))

        
        allMoves.append((numPos[0] - 2*i, numPos[1] - i))
        break

    
    validMoves = []
    for T in allMoves:
        if T in board:
            validMoves.append(boardPairings[T])

    validMoves.sort()
    return validMoves


print(*knight_moves(user))
