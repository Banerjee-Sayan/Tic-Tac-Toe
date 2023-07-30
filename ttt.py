import sys
def printboard(board):
    for row in board:
        for element in row:
            print(element, end=' ')
        print() 
def checkwinner(board, input):
    if (board[0][0] == input and board[0][1] == input and board[0][2] == input) or \
       (board[1][0] == input and board[1][1] == input and board[1][2] == input) or \
       (board[2][0] == input and board[2][1] == input and board[2][2] == input):
        print(f"{input} is the winner")
        print("Game Over")
        sys.exit(0)
    elif (board[0][0] == input and board[1][0] == input and board[2][0] == input) or \
         (board[0][1] == input and board[1][1] == input and board[2][1] == input) or \
         (board[0][2] == input and board[1][2] == input and board[2][2] == input):
        print(f"{input} is the winner")
        print("Game Over")
        sys.exit(0)
    elif (board[0][0] == input and board[1][1] == input and board[2][2] == input) or \
         (board[0][2] == input and board[1][1] == input and board[2][0] == input):
        print(f"{input} is the winner")
        print("Game Over")
        sys.exit(0)

def checkdraw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return 0
    return 1        
if __name__ == '__main__': 
    print("Welcome to Tic Tac toe Game")
    print("Board is as Shown Below")
    board1 = [['1','2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    printboard(board1)
    
    board = [['-','-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    row =3
    col=3
    totalmove= row*col
    move=0
    turn=0
    while(1):
        
        if turn ==0:
            n = int(input("Enter Position for X"))
            rownumber = int((n - 1) / col);
            colnumber = int((n - 1) % col);
            if (0 <= rownumber < row)  and (0 <= colnumber < col) and (board[rownumber][colnumber] == '-'):
                board[rownumber][colnumber] = 'x';
                move=move+1
            else:
                print("Invalid Position")
                continue
            printboard(board)    
            checkwinner(board,'x') 
            drawcheck = checkdraw(board)
            if drawcheck ==1:
                print("Game Drawn! ")
                sys.exit(0)   
        else:
            n = int(input("Enter Position for O"))
            rownumber = int((n - 1) / col);
            colnumber = int((n - 1) % col);
            if (0 <= rownumber < row)  and (0 <= colnumber < col) and (board[rownumber][colnumber] == '-'):
                board[rownumber][colnumber] = 'o';
                move=move+1
            else:
                print("Invalid Position")
                continue
            printboard(board)    
            checkwinner(board,'o') 
            drawcheck = checkdraw(board)
            if drawcheck ==1:
                print("Game Drawn! ")
                sys.exit(0)  
       
        if move==totalmove:
            break
        turn = 1-turn  
       
        
        