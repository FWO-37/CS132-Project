class board:
    def __init__(self):
        self.newBoard = [[" "," "," "],[" "," "," "],[" "," "," "]] # initializing board as list of lists
    
    def __str__(self): # creating cleaner board
        return f'{self.newBoard[0][0]}_|_{self.newBoard[0][1]}_|_{self.newBoard[0][2]}\n{self.newBoard[1][0]}_|_{self.newBoard[1][1]}_|_{self.newBoard[1][2]}\n{self.newBoard[2][0]} | {self.newBoard[2][1]} | {self.newBoard[2][2]}'
        
    __repr__=__str__ 

    def move(self,row,col,player): # the move function, which sets a player symbol to a given location
        if self.newBoard[row][col] == ' ': # if space is empty
            if player == 1: # player 1 is always X
                self.newBoard[row][col] = "X"
            elif player == 2: # player 2 is always Y
                self.newBoard[row][col] = "O"
            else:
                print("invalid player number")
        else: 
            print("try again") # if the space isn't empty, it reruns the function using new inputs
            newrow = int(input(f"What row (0-2) would you like to move in player {player}?: "))
            newcol = int(input(f"What col (0-2) would you like to move in player {player}?: "))
            self.move(newrow,newcol,player)

    def full(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.newBoard[i][j] == 'X' or self.newBoard[i][j] == 'O': # if every space is full with a user symbol
                    count += 1
        if count == 9:
            return True # all spaces full
        return False

    def check_winner(self,player):
        if player == 1:
            # rows
            if (self.newBoard[0][0] == self.newBoard[0][1] == self.newBoard[0][2]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[1][0] == self.newBoard[1][1] == self.newBoard[1][2]) and self.newBoard[1][0] == 'X':
                return True
            if (self.newBoard[2][0] == self.newBoard[2][1] == self.newBoard[2][2]) and self.newBoard[2][0] == 'X':
                return True
            # cols
            if (self.newBoard[0][0] == self.newBoard[1][0] == self.newBoard[2][0]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[0][1] == self.newBoard[1][1] == self.newBoard[2][1]) and self.newBoard[0][1] == 'X':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][2] == self.newBoard[2][2]) and self.newBoard[0][2] == 'X':
                return True
            # diagonals
            if (self.newBoard[0][0] == self.newBoard[1][1] == self.newBoard[2][2]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][1] == self.newBoard[2][0]) and self.newBoard[0][2] == 'X':
                return True
        if player == 2:
            # rows
            if (self.newBoard[0][0] == self.newBoard[0][1] == self.newBoard[0][2]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[1][0] == self.newBoard[1][1] == self.newBoard[1][2]) and self.newBoard[1][0] == 'O':
                return True
            if (self.newBoard[2][0] == self.newBoard[2][1] == self.newBoard[2][2]) and self.newBoard[2][0] == 'O':
                return True
            # cols
            if (self.newBoard[0][0] == self.newBoard[1][0] == self.newBoard[2][0]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[0][1] == self.newBoard[1][1] == self.newBoard[2][1]) and self.newBoard[0][1] == 'O':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][2] == self.newBoard[2][2]) and self.newBoard[0][2] == 'O':
                return True
            # diagonals
            if (self.newBoard[0][0] == self.newBoard[1][1] == self.newBoard[2][2]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][1] == self.newBoard[2][0]) and self.newBoard[0][2] == 'O':
                return True
        return False
    
    def game(self):
        move = 0 # starting move
        while (self.full() == False) and (self.check_winner(1) == False) and (self.check_winner(2) == False): # while not tie or win
            print(self) # prints out board so visual is provided
            if move%2 == 0: # while player 1s move
                row = int(input("What row (0-2) would you like to move in player 1?: ")) # takes row input
                while row > 3 or row < 0: # resets if necessary
                    row = int(input("Try again. What row (0-2) would you like to move in player 1?: "))
                col = int(input("What col (0-2) would you like to move in player 1?: ")) # takes col input
                while col > 3 or col < 0: # resets if necessary
                    col = int(input("Try again. What col (0-2) would you like to move in player 1?: "))
                self.move(row,col,1) # makes the move
                move += 1
            else:
                row = int(input("What row (0-2) would you like to move in player 2?: ")) # takes row input
                while row > 3 or row < 0: # resets if necessary
                    row = int(input("Try again. What row (0-2) would you like to move in player 2?: "))
                col = int(input("What col (0-2) would you like to move in player 2?: ")) # takes col input
                while col > 3 or col < 0: # resets if necessary              
                    col = int(input("Try again. What col (0-2) would you like to move in player 2?: "))
                self.move(row,col,2) # makes the move
                move += 1 # increments number of moves
        print(self) # prints final board
        if self.check_winner(1) == True: # prints final result
            print("player 1 wins!")
        elif self.check_winner(2) == True:
            print("player 2 wins!")
        else: 
            print("You both lose")
              
def print_board(board): # print_board function
        print(board) # prints the clean board

def check_winner(board,player):
        return(board.check_winner(player)) # returns if the specific player won
        
def full(board):
    return board.full() # returns if the board is full

def is_draw(board):
    if full(board) == True: # if the board is full
        if board.check_winner(1) == False and board.check_winner(2) == False: # and there is no winner
            return True
    return False

    
