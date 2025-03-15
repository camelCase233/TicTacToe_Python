def makeBoard():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board
def printBoard(board):
    for row in board:
        print(row)
    return

class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.moves = []

def makePlayer(name, sign):
    return Player(name, sign)

def checkWinner(player):
    winningArray = [[0,3,6], [0,4,8], [0,1,2], [1,4,7], [3,4,5], [6,7,8], [2,5,8], [2,4,6]]
    for combo in winningArray:
        if all(move in player.moves for move in combo):
            return True
    return False

def makeMove(player, board, index):
    i = index//3
    j = index%3
    if board[i][j] == " ":
        board[i][j] = player.sign
        player.moves.append(index)
        return True
    return False

def checkDraw(board, player_one, player_two):
    if not checkWinner(player_one) and not checkWinner(player_two):
        if all(cell != " " for row in board for cell in row):
            return True
    return False


def play():
    gamePlay = True
    name = input("Enter your name, the worthy player one\n")
    player_one = makePlayer(name, 'X')
    name_two = input("Enter your name, the unworthy player_two\n")
    player_two = makePlayer(name_two, 'O')
    turn_playerone = True
    board = makeBoard()

    while gamePlay == True:
        if turn_playerone == True:
            try:
                index = int(input(f"The worthy almighty {player_one.name}, what the index shall be?"))
                if makeMove(player_one, board, index):
                    printBoard(board)
                    turn_playerone = False
                    if checkWinner(player_one):
                        print(f"{player_one.name} has won yay")
                        gamePlay = False
                        return
                else:
                    print('That index is already full, you idiot')
            except (ValueError, IndexError):
                print("Bruh, enter a valid index, between 0 and 8")
        
        else:
            try:
                index = int(input(f"What index will you use {player_two.name}?"))
                if makeMove(player_two, board, index):
                    printBoard(board)
                    turn_playerone = True
                    if checkWinner(player_two):
                        print(f"Ewwwwww {player_two.name} has won, eww")
                        gamePlay = False
                        return
                else:
                    print('That index is already full, you idiot')
            except (ValueError, IndexError):
                print("Bruh, enter a valid index, between 0 and 8")
        
        if checkDraw(board, player_one, player_two):
            print("It's a draw guys")

play()