# Game board 
BOARD_COLS = 5  # Change here if you want wider Game board
BOARD_ROWS = 5  # Change here if you want higher Game board

class board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.turns = 0
        self.lastMove = [-1, -1] # [r, c]

    def drawBoard(self):
        print("\n")
        # Nummeration of the cols 
        for r in range(BOARD_COLS):
            print(f"  ({r+1})     ", end="        ")
        print("\n")

        # The seperation of the playing fields
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"        {self.board[r][c]}      |", end="")
            print("\n")

        print(f"{'-' * 60}\n")

    def whoseTurn(self):
        players = ['(\U0001f49a)','[\U0001f9e1]']
        return players[self.turns % 2]
    
    def borders(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)

    def turn(self, column):
        # Look at the bottom line for free space
        for i in range(BOARD_ROWS-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.whoseTurn()
                self.lastMove = [i, column]

                self.turns += 1
                return True

        return False

    def determineWinner(self):
        lastRow = self.lastMove[0]
        lastCol = self.lastMove[1]
        lastPoint = self.board[lastRow][lastCol]

        # checking directions which can be true for positioned points
        directions = [[[-1, 0], 0, True], 
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],
                      [[0, 1], 0, True],
                      [[-1, -1], 0, True],
                      [[1, 1], 0, True],
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        # Check for Pieces that match
        for a in range(4):
            for d in directions:
                r = lastRow + (d[0][0] * (a+1))
                c = lastCol + (d[0][1] * (a+1))

                if d[2] and self.borders(r, c) and self.board[r][c] == lastPoint:
                    d[1] += 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Check pieces in a row'
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 4):  # Change here if you want more or less point to win (to change >= 'number' (example >= 3 --> 4 in a row win, >= 4 --> 5 in a row win))
                self.drawBoard()
                print(f"{lastPoint} is the winner!")
                #list = [f"{lastPoint}"]
                #count = list.numbers()
                #print(count)
                return lastPoint   

        # No winner
        return False

def play():
    # Game Board
    game = board()

    gameOver = False

    while not gameOver:
        game.drawBoard()

        # input valid numbers 
        correctMove = False
        while not correctMove:
            playerMove = input(f"{game.whoseTurn()}'s Turn!! \nChoose a cole (1-{BOARD_COLS}): ")
            try:
                correctMove = game.turn(int(playerMove)-1)
            except:
                print(f"Number invalid! \nPlease choose a number between 1 and {BOARD_COLS}")

        # Game is ending if winner found
        gameOver = game.determineWinner()
        
        # nobody won
        if not any(' ' in x for x in game.board):
            print("\n\U0001f4a5 The game is a tie...\U0001f4a5")
            return

# Approach for Singelton?
class stats():
    def __statistics__():
        return  

# A role model for the class login was the DesignPattern "Facade"
class login:
    def __init__(self):
        self.credintials = {}

    def register(self, username, password):
        self.credintials[username] = password
        print("Your ragestration was a success! ")
        stop = False

        while stop == False:
            print("\nWhat would you like to do : ")
            print("\n1 - Play\n2 - Stats\n3 - Quit")
            taskSecond = input("Enter you option here : ")
            if taskSecond == '1':
                play()
            if taskSecond == '2':
                print("\nNot available...")
            if taskSecond == '3':
                print("\nBack to Home!")
                stop = True

    def check(self, username, password):
        print(self.credintials)
        if username in self.credintials.keys() and password == self.credintials[username]:
            print("Login success! ")
            stop = False

            while stop == False:
                print("\nWhat would you like to do : ")
                print("\n1 - Play\n2 - Stats\n3 - Quit")
                taskThird = input("Enter you option here : ")
                if taskThird == '1':
                    play()
                if taskThird == '2':
                    print("\nNot available...")
                if taskThird == '3':
                    print("\nBack to Home!")
                    stop = True
                
        else:
            print('\nWrong Username or Password! ')

data = login()

stop = False

while stop == False:
    print("\n\U0001f4ab Welcome to ConnectFour \U0001f4ab")
    print("\nWhat would you like to do :")
    print("\n1 - \U0000265f  Play a Game \U0000265f\n2 - \U0001f50f  Login \U0001f50f\n3 - \U0001f58a  Register \U0001f58a\n4 - \U0000274c  Quit \U0000274c")
    taskFirst = input("Enter you option here : ")
        # Calling functions with that class object
    if taskFirst == '1':
        play() 

    if taskFirst == '2':
        registeredUsername = (input('\nUsername : '))
        regesteredPassword = (input('Password : '))
        data.check(registeredUsername, regesteredPassword)

    if taskFirst == '3':
        username = (input('\nUsername : '))
        password = (input('Password : '))
        data.register(username, password)

        
    if taskFirst == '4':
        print("\n\U0001f64b Bye Bye, hope you play sometime again! \U0001f64b")
        stop = True


