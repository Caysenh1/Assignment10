def run():
    word = input("Choose a piece: ")
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

    if word == 'rook' or word == 'ROOK' or word == 'Rook':
        def rook_moves(pos):
    # Convert 'e4' into (5,4)
            first = 'abcdefgh'
            second = '12345678'
            numPos = (first.index(pos[0]) + 1, int(pos[1]))

    # Numeric board
            board = []
            for i in range(1,9):
                for j in range(1,9):
                    board.append((i,j))

    # Alpha board
            alphaBoard = []
            for letter in first:
                for number in second:
                    alphaBoard.append(f"{letter}{number}")

    
            boardPairings = dict(zip(board, alphaBoard))

            allMoves = []
            for i in range(1,8):
        # (5,4) -> (6,4), etc.
                allMoves.append((numPos[0] + i, numPos[1]))

        # (5,4) -> (5,5), etc.
                allMoves.append((numPos[0], numPos[1] + i))

        # (5,4) -> (4,4), etc.
                allMoves.append((numPos[0] - i, numPos[1]))

        # (5,4) -> (5,3), etc.
                allMoves.append((numPos[0], numPos[1] - i))

  
            validMoves = []
            for T in allMoves:
                if T in board:
                    validMoves.append(boardPairings[T])

            validMoves.sort()
            return validMoves


        print(*rook_moves(user))
    if word == 'king' or word == 'KING' or word == 'King':
        def king_moves(pos):
            first = 'abcdefgh'
            second = '12345678'
            numPos = first.index(pos[0]) + 1, int(pos[1])

            board = []
            for i in range(1,9):
                for j in range(1,9):
                    board.append((i,j))

            alphaboard = []
            for letter in first:
                for number in second:
                    alphaboard.append(f"{letter}{number}")

            boardPairings = dict(zip(board, alphaboard))

            allMoves = []
            for i in range(1,8):
        #(5,4) -> (6,4)
                allMoves.append((numPos[0] + i , numPos[1]))
        
        #(5,4) -> (6,5)
                allMoves.append((numPos[0] + i, numPos[1] + i))
        
        #(5,4) -> (5,5)
                allMoves.append((numPos[0], numPos[1] + i))
        
        #(5,4) -> (6,3)
                allMoves.append((numPos[0] + i, numPos[1] - i))
        
        #(5,4) -> (5,3)
                allMoves.append((numPos[0], numPos[1] - i))
        
        #(5,4) -> (4,4)
                allMoves.append((numPos[0] - i, numPos[1] - i))
        
        #(5,4) -> (4,5)
                allMoves.append((numPos[0] - i, numPos[1] + i))
        
        #(5,4) -> (4,3)
                allMoves.append((numPos[0] - i, numPos[1]))
                break
     
            validMoves = []
            for T in allMoves:
                if T in board:
                    validMoves.append(boardPairings[T])

            validMoves.sort()
            return validMoves
        print(*king_moves(user))
    if word == 'bishop' or word == 'BISHOP' or word == 'Bishop':
        def bishop_moves(pos):
    
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
        
                allMoves.append((numPos[0] + i, numPos[1] + i))

        
                allMoves.append((numPos[0] - i, numPos[1] + i))

        
                allMoves.append((numPos[0] - i, numPos[1] - i))

        
                allMoves.append((numPos[0] + i, numPos[1] - i))

    
            validMoves = []
            for T in allMoves:
                if T in board:
                    validMoves.append(boardPairings[T])

            validMoves.sort()
            return validMoves


        print(*bishop_moves(user))
    if word == 'knight' or word == 'KNIGHT' or word == 'Knight':
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
    if word == 'queen' or word == 'QUEEN' or word=='Queen':
        def queen_moves(pos):
            first = 'abcdefgh'
            second = '12345678'
            numPos = first.index(pos[0]) + 1, int(pos[1])
    
            board = []
            for i in range(1,9):
                for j in range(1,9):
                    board.append((i,j))

            alphaboard = []
            for letter in first:
                for number in second:
                    alphaboard.append(f"{letter}{number}")

            boardPairings = dict(zip(board, alphaboard))

            allMoves = []
            for i in range(1,8):
        
                allMoves.append((numPos[0] + i , numPos[1]))
        
        
                allMoves.append((numPos[0] + i, numPos[1] + i))
        
        
                allMoves.append((numPos[0], numPos[1] + i))
        
            
                allMoves.append((numPos[0] + i, numPos[1] - i))
        
        
                allMoves.append((numPos[0], numPos[1] - i))
        
        
                allMoves.append((numPos[0] - i, numPos[1] - i))
        
        
                allMoves.append((numPos[0] - i, numPos[1] + i))
        
            
                allMoves.append((numPos[0] - i, numPos[1]))
        
    
            validMoves = []
            for T in allMoves:
                if T in board:
                    validMoves.append(boardPairings[T])

            validMoves.sort()
            return validMoves
        print(*queen_moves(user))
    





