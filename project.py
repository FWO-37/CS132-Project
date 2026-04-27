class board:
    def __init__(self):
        gameNumber = 0
        turnNumber = 0
        self.newBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    def __str__(self):
        return f'{self.newBoard[0][0]}_|_{self.newBoard[0][1]}_|_{self.newBoard[0][2]}\n{self.newBoard[1][0]}_|_{self.newBoard[1][1]}_|_{self.newBoard[1][2]}\n{self.newBoard[2][0]} | {self.newBoard[2][1]} | {self.newBoard[2][2]}'
        
    __repr__=__str__

    def current(self,row,col):
        return self.newBoard[row][col]

    def move(self,row,col,player):
        if self.newBoard[row][col] == ' ':
            if player == 1:
                self.newBoard[row][col] = "X"
            elif player == 2:
                self.newBoard[row][col] = "O"
            else:
                print("invalid player number")
        else: 
            print("try again")
            newrow = int(input(f"What row (0-2) would you like to move in player {player}?: "))
            newcol = int(input(f"What col (0-2) would you like to move in player {player}?: "))
            self.move(newrow,newcol,player)

    def full(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.newBoard[i][j] == 'X' or self.newBoard[i][j] == 'O':
                    count += 1
        if count == 9:
            return True
        return False

    def check_winner(self,player):
        if player == 1:
            if (self.newBoard[0][0] == self.newBoard[0][1] == self.newBoard[0][2]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[1][0] == self.newBoard[1][1] == self.newBoard[1][2]) and self.newBoard[1][0] == 'X':
                return True
            if (self.newBoard[2][0] == self.newBoard[2][1] == self.newBoard[2][2]) and self.newBoard[2][0] == 'X':
                return True
            if (self.newBoard[0][0] == self.newBoard[1][0] == self.newBoard[2][0]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[0][1] == self.newBoard[1][1] == self.newBoard[2][1]) and self.newBoard[0][1] == 'X':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][2] == self.newBoard[2][2]) and self.newBoard[0][2] == 'X':
                return True
            if (self.newBoard[0][0] == self.newBoard[1][1] == self.newBoard[2][2]) and self.newBoard[0][0] == 'X':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][1] == self.newBoard[2][0]) and self.newBoard[0][2] == 'X':
                return True
        if player == 2:
            if (self.newBoard[0][0] == self.newBoard[0][1] == self.newBoard[0][2]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[1][0] == self.newBoard[1][1] == self.newBoard[1][2]) and self.newBoard[1][0] == 'O':
                return True
            if (self.newBoard[2][0] == self.newBoard[2][1] == self.newBoard[2][2]) and self.newBoard[2][0] == 'O':
                return True
            if (self.newBoard[0][0] == self.newBoard[1][0] == self.newBoard[2][0]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[0][1] == self.newBoard[1][1] == self.newBoard[2][1]) and self.newBoard[0][1] == 'O':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][2] == self.newBoard[2][2]) and self.newBoard[0][2] == 'O':
                return True
            if (self.newBoard[0][0] == self.newBoard[1][1] == self.newBoard[2][2]) and self.newBoard[0][0] == 'O':
                return True
            if (self.newBoard[0][2] == self.newBoard[1][1] == self.newBoard[2][0]) and self.newBoard[0][2] == 'O':
                return True
        return False
    
    def game(self):
        move = 0
        print(self.full())
        print(self.check_winner(1))
        print(self.check_winner(2))
        while (self.full() == False) and (self.check_winner(1) == False) and (self.check_winner(2) == False):
            print(self)
            if move%2 == 0:
                row = int(input("What row (0-2) would you like to move in player 1?: "))
                while row > 3 or row < 0:                
                    row = int(input("Try again. What row (0-2) would you like to move in player 1?: "))
                col = int(input("What col (0-2) would you like to move in player 1?: "))
                while col > 3 or col < 0:                
                    col = int(input("Try again. What col (0-2) would you like to move in player 1?: "))
                self.move(row,col,1)
                move += 1
            else:
                row = int(input("What row (0-2) would you like to move in player 2?: "))
                while row > 3 or row < 0:                
                    row = int(input("Try again. What row (0-2) would you like to move in player 2?: "))
                col = int(input("What col (0-2) would you like to move in player 2?: "))
                while col > 3 or col < 0:                
                    col = int(input("Try again. What col (0-2) would you like to move in player 2?: "))
                self.move(row,col,2)
                move += 1
        print(self)
        if self.check_winner(1) == True:
            print("player 1 wins!")
        elif self.check_winner(2) == True:
            print("player 2 wins!")
        else: 
            print("You both lose")
              
def print_board(board):
        print(board)

def check_winner(board,player):
        return(board.check_winner(player))
        
def full(board):
    return board.full()

def is_draw(board):
    if full(board) == True:
        if board.check_winner(1) == False and board.check_winner(2) == False:
            return True
    return False


if __name__ == "__main__":
    new = board()
    new.game()

    
