"""
This is a program that creates a Chess game in
Python using the graphics library. The program
is composed of three main classes: Piece,
ChessBoard, and ChessGame. The Piece class
creates chess pieces with the properties of
name, color, position, and whether it has moved.
The ChessBoard class creates an 8x8 board and
populates it with chess pieces in their starting
positions. The ChessGame class creates an instance
of the ChessBoard and uses it to run the game.
It includes methods for moving pieces, checking
for checkmate, and drawing the board and pieces
on the screen. The game can be run by calling
the run() method on an instance of the ChessGame class.
"""
from graphics import *

"""
This code defines the Piece class in Python.
The class has a constructor method (__init__)
that takes in three arguments: name, color, and
position. These arguments are used to initialize
the instance variables self.name, self.color,
self.position, and self.has_moved. The
self.has_moved variable is set to False by
default, indicating that the piece has not moved
yet.
"""
class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position
        self.has_moved = False

"""
This code defines the ChessBoard class in Python.
The class has a constructor method (__init__) that
initializes an 8x8 board with all elements set to
None, then calls the populate_board method. The
populate_board method populates the board with
chess pieces in their starting positions, with
rooks in the corners, knights and bishops next
to them, queen and king in the middle, and pawns
in the second and seventh row. The class also
defines a get_piece_at_position method which takes
in a row and col and returns the piece at that
position on the board. The move_piece method
takes in the coordinates of a piece's current
position and the coordinates of its destination
and moves the piece to the destination,
updating the piece's position and marking it
as having moved.
"""
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def populate_board(self):
        self.board[0][0] = Piece("rook", "white", (0, 0))
        self.board[0][1] = Piece("knight", "white", (0, 1))
        self.board[0][2] = Piece("bishop", "white", (0, 2))
        self.board[0][3] = Piece("queen", "white", (0, 3))
        self.board[0][4] = Piece("king", "white", (0, 4))
        self.board[0][5] = Piece("bishop", "white", (0, 5))
        self.board[0][6] = Piece("knight", "white", (0, 6))
        self.board[0][7] = Piece("rook", "white", (0, 7))

        self.board[7][0] = Piece("rook", "black", (7, 0))
        self.board[7][1] = Piece("knight", "black", (7, 1))
        self.board[7][2] = Piece("bishop", "black", (7, 2))
        self.board[7][3] = Piece("queen", "black", (7, 3))
        self.board[7][4] = Piece("king", "black", (7, 4))
        self.board[7][5] = Piece("bishop", "black", (7, 5))
        self.board[7][6] = Piece("knight", "black", (7, 6))
        self.board[7][7] = Piece("rook", "black", (7, 7))

        for i in range(8):
            self.board[1][i] = Piece("pawn", "white", (1, i))
            self.board[6][i] = Piece("pawn", "black", (6, i))

    def get_piece_at_position(self, row, col):
        return self.board[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        self.board[from_row][from_col] = None
        self.board[to_row][to_col] = piece
        self.board[to_row][to_col].position = (to_row, to_col)
        self.board[to_row][to_col].has_moved = True
        return

"""
This code defines the ChessGame class
in Python. The class has a constructor
method (__init__) that creates an instance
of the ChessBoard class and initializes
several instance variables like self.selected_piece,
self.white_score, self.black_score,
self.drawing_list, and self.turn. The run method
is the main loop of the game that keeps the game
running until it is checkmate or the player closes
the game. In this method, the game checks if the
game is in checkmate state and if so, it return.
It also draws the board and pieces on the screen,
gets user input to select the piece and its
destination, moves the selected piece to the
destination and change the turn. The method
draw_board is used to draw the chess board on
the screen and the method draw_pieces to draw
the chess pieces on the screen. The method
select_a_position is used to get user input for
selecting a piece or its destination and it returns
the selected position. The method select_piece is
used to select a piece and the method move_selected_piece
is used to move the selected piece to the destination.
"""
class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.selected_piece = None
        self.white_score = 0
        self.black_score = 0
        self.drawing_list = []
        self.win = self.draw_board()
        self.turn = "white"

    """
    This code defines the run method of the ChessGame class,
    which is the main loop of the game. It checks if the game
    is in a checkmate state, redraws the board, and waits
    for user input to select a piece and its destination.
    If a valid move is made, the turn is changed and the
    loop continues. If an invalid move is made, the player
    must select again. The try-except block is used to handle
    any unexpected errors.
    """
    def run(self):
        running = True
        while running:
            try:
                if (self.is_checkmate("white") or self.is_checkmate("black")):
                    return
                # redraw the board
                self.draw_pieces()
                moved = False
                while (moved!=True):
                    # get user click and convert click to board position
                    row, col = self.select_a_position()
                    self.select_piece(row, col)
                    # if a piece is selected
                    if (self.selected_piece is not None) and (self.selected_piece.color==self.turn):
                        # move the piece to the clicked position and convert click to
                        # board position
                        row, col = self.select_a_position()
                        if (self.move_selected_piece(row, col)):
                            self.selected_piece = None
                            moved = True
                            if (self.turn == "white"):
                                self.turn = "black"
                            elif (self.turn == "black"):
                                self.turn = "white"
                        else:
                            moved = False
            except:
                running = False

    """
    This code defines the draw_board method, which is
    responsible for drawing the chess board on the screen
    using the graphics library. It creates a window with
    a title "Chess Game" and dimensions 400x400, then it
    uses nested for-loops to create rectangles that
    represent each square of the chess board. It sets the
    fill color of the rectangles to be alternate between
    two colors, depending on the position of the square,
    to create the chess board pattern. The rectangles are
    then drawn on the window and the method returns the
    window object.
    """
    def draw_board(self):
        win = GraphWin("Chess Game", 400, 400)
        for i in range(8):
            for j in range(8):
                rect = Rectangle(Point(50*j, 50*i), Point(50*(j+1), 50*(i+1)))
                if (i+j) % 2 == 0:
                    rect.setFill("#ECECEC")
                else:
                    rect.setFill("#878787")
                rect.draw(win)
        return win

    """
    This method is responsible for drawing the chess pieces
    on the board. It first undraws any existing pieces on
    the board, then iterates through the board's positions
    and if a piece exists in that position, it creates a shape
    based on the piece's name and color, sets its fill color,
    and draws it on the board. It also keeps track of the
    shapes by adding them to the drawing_list.
    """
    def draw_pieces(self):
        for shape in self.drawing_list:
            shape.undraw()
        for i in range(8):
            for j in range(8):
                piece = self.board.get_piece_at_position(i, j)
                if piece is not None:
                    if piece.color == "white":
                        color = "white"
                    else:
                        color = "black"
                    if piece.name == "pawn":
                        shape = Circle(Point(25+50*j, 25+50*i), 15)
                    elif piece.name == "rook":
                        shape = Rectangle(Point(10+50*j, 10+50*i), Point(40+50*j, 40+50*i))
                    elif piece.name == "knight":
                        shape = Polygon(Point(25+50*j, 10+50*i), Point(40+50*j, 25+50*i), Point(25+50*j, 40+50*i), Point(10+50*j, 25+50*i))
                    elif piece.name == "bishop":
                        shape = Polygon(Point(10+50*j, 10+50*i), Point(40+50*j, 40+50*i), Point(40+50*j, 10+50*i), Point(10+50*j, 40+50*i))
                    elif piece.name == "queen":
                        shape = Circle(Point(25+50*j, 25+50*i), 20)
                    elif piece.name == "king":
                        shape = Circle(Point(25+50*j, 25+50*i), 25)
                    shape.setFill(color)
                    shape.draw(self.win)
                    self.drawing_list.append(shape)
        return self.drawing_list

    """
    This function waits for the user to click within the game
    window, then converts the x,y coordinates of the click
    to a row,col position on the chess board and returns it.
    """
    def select_a_position(self):
        click = self.win.getMouse()
        col = int(click.getX() // 50)
        row = int(click.getY() // 50)
        return (row, col)

    """
    This method takes in the row and col of a chess board
    position and checks if there is a piece at that position.
    If there is, it sets the selected_piece attribute of the
    ChessGame class to the piece at that position and returns
    True. If there is no piece at the position, it returns False.
    """
    def select_piece(self, row, col):
        if self.board.get_piece_at_position(row, col) is not None:
            self.selected_piece = self.board.get_piece_at_position(row, col)
            return True
        else:
            return False

    """
    This method updates the score of the game, by checking if a
    piece is captured, and if so, incrementing the score of the
    opposing player by 1. The captured piece's color is compared
    to the selected piece's color to determine which player's score
    should be incremented. The return statement at the end is not
    necessary as the function has a void return type.
    Note: In actual chess the points for capturing a piece depend
    on the type of piece captured, but this is simplified for the
    sake of creating a basic implementation of the game
    """
    def update_score(self, row, col):
        captured_piece = self.board.get_piece_at_position(row, col)
        if captured_piece is not None and captured_piece.color != self.selected_piece.color:
            if self.selected_piece.color == "white":
                self.white_score += 1
            else:
                self.black_score += 1
        return

    """
    The move_selected_piece function is responsible for moving
    the selected piece to a new position on the chess board.
    It first checks if a piece is actually selected, and if so
    it checks if the move is valid using the is_valid_move function.
    If the move is valid it will move the piece to the new position,
    if the piece is a pawn and it reaches the other side of the board,
    it will ask the user to promote it to a different piece. If the
    move is not valid, it will return False. It also checks if the move
    is a castle move, and if so it will move the king and the rook
    accordingly and return True. If a piece is captured, it will
    update the score.
    """
    def move_selected_piece(self, row, col):
        if self.selected_piece is not None:
            if self.is_valid_move(self.selected_piece, row, col):
                castle = False
                if self.selected_piece.name == "king" and self.selected_piece.has_moved == False:
                    curr_row, curr_col = self.selected_piece.position
                    if (row == curr_row and col == curr_col+3 and self.board.get_piece_at_position(curr_row, curr_col+1) == None and self.board.get_piece_at_position(curr_row, curr_col+2) == None and self.board.get_piece_at_position(curr_row, curr_col+3).has_moved == False and self.board.get_piece_at_position(curr_row, curr_col+3).name == "rook" and self.board.get_piece_at_position(curr_row, curr_col+3).color == self.selected_piece.color):
                        self.board.move_piece(self.selected_piece.position[0], self.selected_piece.position[1], curr_row, curr_col+2)
                        self.board.move_piece(curr_row, curr_col+3, curr_row, curr_col+1)
                        self.selected_piece = None
                        castle = True
                        return True
                    elif (row == curr_row and col == curr_col-4 and self.board.get_piece_at_position(curr_row, curr_col-1) == None and self.board.get_piece_at_position(curr_row, curr_col-2) == None and self.board.get_piece_at_position(curr_row, curr_col-3) == None and self.board.get_piece_at_position(curr_row, curr_col-4).has_moved == False and self.board.get_piece_at_position(curr_row, curr_col-4).name == "rook" and self.board.get_piece_at_position(curr_row, curr_col-4).color == self.selected_piece.color):
                        self.board.move_piece(self.selected_piece.position[0], self.selected_piece.position[1], curr_row, curr_col-2)
                        self.board.move_piece(curr_row, curr_col-4, curr_row, curr_col-1)
                        self.selected_piece = None
                        castle = True
                        return True
                if not castle:
                    captured_piece = self.board.get_piece_at_position(row, col)
                    if captured_piece is not None:
                        if captured_piece.color == "white":
                            self.black_score += 1
                        else:
                            self.white_score += 1

                    self.board.move_piece(self.selected_piece.position[0], self.selected_piece.position[1], row, col)
                    if (self.selected_piece.name == "pawn"):
                        if ((self.selected_piece.color == "white" and row == 7) or (self.selected_piece.color == "black" and row == 0)):
                            promotion = str(input("What would you like to promote your pawn to? (queen, knight, rook, bishop)"))
                            if (((promotion=="queen") or(promotion=="knight")) or ((promotion=="rook") or (promotion=="bishop"))):
                                self.selected_piece.name = promotion
                    self.selected_piece = None
                    return True
            else:
                return False
        else:
            return False

    """
    This method is checking whether a move for a certain chess
    piece is valid or not. It first checks the type of piece
    (pawn, rook, knight, bishop, queen, king) and calls the
    corresponding function to check if the move is valid. If
    the move is valid it then checks if the move will put the
    king in check or not, and returns true if the move is valid
    and doesn't put king in check, returns false otherwise.
    """
    def is_valid_move(self, piece, row, col):
        valid = False
        if piece.name == "pawn":
            valid = self.is_valid_pawn_move(piece, row, col)
        elif piece.name == "rook":
            valid = self.is_valid_rook_move(piece, row, col)
        elif piece.name == "knight":
            valid = self.is_valid_knight_move(piece, row, col)
        elif piece.name == "bishop":
            valid = self.is_valid_bishop_move(piece, row, col)
        elif piece.name == "queen":
            valid = self.is_valid_queen_move(piece, row, col)
        elif piece.name == "king":
            valid = self.is_valid_king_move(piece, row, col)
        if valid:
            currRow = piece.position[0]
            currCol = piece.position[1]
            copy_of_board = [[None for _ in range(8)] for _ in range(8)]
            for i in range(len(self.board.board)):
                for j in range(len(self.board.board)):
                    copy_of_board[i][j] = self.board.board[i][j]
            move_status = self.board.board[currRow][currCol].has_moved
            self.board.move_piece(currRow, currCol, row, col)
            valid = not self.is_in_check(piece.color)
            self.board.move_piece(row, col, currRow, currCol)
            self.board.board = copy_of_board
            self.board.board[currRow][currCol].has_moved = move_status
            if valid:
                return True
        return False

    """
    This code is a method for checking if a move made by a
    pawn piece is valid. It checks the color of the piece,
    the position of the piece, and the destination of the
    move to determine if it is a valid move. It also checks
    if the destination square is occupied by an opposing
    color piece, and if so, it is a valid move. If the move
    is valid, it returns True, otherwise, it returns False.
    """
    def is_valid_pawn_move(self, piece, row, col):
        if piece.color == "white":
            if piece.position[0] == 1:
                if (row == piece.position[0] + 2 and col == piece.position[1] and self.board.get_piece_at_position(row-1, col) == None and self.board.get_piece_at_position(row, col) == None):
                    return True
                elif (row == piece.position[0] + 1 and col == piece.position[1] and self.board.get_piece_at_position(row, col) == None):
                    return True
                elif (row == piece.position[0] + 1 and abs(col - piece.position[1]) == 1 and self.board.get_piece_at_position(row, col) != None and self.board.get_piece_at_position(row, col).color == "black"):
                    return True
            elif (row == piece.position[0] + 1 and col == piece.position[1] and self.board.get_piece_at_position(row, col) == None):
                return True
            elif (row == piece.position[0] + 1 and abs(col - piece.position[1]) == 1 and self.board.get_piece_at_position(row, col) != None and self.board.get_piece_at_position(row, col).color == "black"):
                return True
            else:
                return False
        else:
            if piece.position[0] == 6:
                if (row == piece.position[0] - 2 and col == piece.position[1] and self.board.get_piece_at_position(row+1, col) == None and self.board.get_piece_at_position(row, col) == None):
                    return True
                elif (row == piece.position[0] - 1 and col == piece.position[1] and self.board.get_piece_at_position(row, col) == None):
                    return True
                elif (row == piece.position[0] - 1 and abs(col - piece.position[1]) == 1 and self.board.get_piece_at_position(row, col) != None and self.board.get_piece_at_position(row, col).color == "white"):
                    return True
            elif (row == piece.position[0] - 1 and col == piece.position[1] and self.board.get_piece_at_position(row, col) == None):
                return True
            elif (row == piece.position[0] - 1 and abs(col - piece.position[1]) == 1 and self.board.get_piece_at_position(row, col) != None and self.board.get_piece_at_position(row, col).color == "white"):
                return True
            else:
                return False

    """
    This is a method that checks if the move of a
    rook piece is valid. It first checks if the
    destination is occupied by a piece of the same
    color. If it is, the move is considered invalid.
    Then it checks if the move is being made horizontally
    or vertically. If it is being made diagonally, it is
    considered invalid. Finally, it checks if there are
    any other pieces in the way of the move, if there
    are the move is considered invalid. If all of these
    checks pass, the move is considered valid.
    """
    def is_valid_rook_move(self, piece, row, col):
        if piece.color == "white":
            if self.board.get_piece_at_position(row,col) and self.board.get_piece_at_position(row,col).color == "white":
                return False
        else:
            if self.board.get_piece_at_position(row,col) and self.board.get_piece_at_position(row,col).color == "black":
                return False
        if piece.position[0] != row and piece.position[1] != col:
            return False
        if piece.position[0] == row:
            start_col = min(piece.position[1],col)
            end_col = max(piece.position[1],col)
            for i in range(start_col+1,end_col):
                if self.board.get_piece_at_position(row,i):
                    return False
        elif piece.position[1] == col:
            start_row = min(piece.position[0],row)
            end_row = max(piece.position[0],row)
            for i in range(start_row+1,end_row):
                if self.board.get_piece_at_position(i,col):
                    return False
        return True

    """
    This code is a method that checks whether a
    move made by a knight is valid. It takes in the
    piece being moved (a knight), the target row and
    column of the move, and checks if the move is a
    valid L-shaped movement (2 spaces in one direction,
    1 space in another direction). It also checks if
    the target space is unoccupied or if it is occupied
    by an opposing colored piece. If the move is valid,
    it returns True, otherwise it returns False.
    """
    def is_valid_knight_move(self, piece, row, col):
        if piece.color == "white":
            if (row == piece.position[0]-2 and col == piece.position[1]-1) or (row == piece.position[0]-2 and col == piece.position[1]+1) or (row == piece.position[0]-1 and col == piece.position[1]-2) or (row == piece.position[0]-1 and col == piece.position[1]+2) or (row == piece.position[0]+1 and col == piece.position[1]-2) or (row == piece.position[0]+1 and col == piece.position[1]+2) or (row == piece.position[0]+2 and col == piece.position[1]-1) or (row == piece.position[0]+2 and col == piece.position[1]+1):
                if self.board.get_piece_at_position(row,col) is None or self.board.get_piece_at_position(row,col).color == 'black':
                    return True
        elif piece.color == "black":
            if (row == piece.position[0]-2 and col == piece.position[1]-1) or (row == piece.position[0]-2 and col == piece.position[1]+1) or (row == piece.position[0]-1 and col == piece.position[1]-2) or (row == piece.position[0]-1 and col == piece.position[1]+2) or (row == piece.position[0]+1 and col == piece.position[1]-2) or (row == piece.position[0]+1 and col == piece.position[1]+2) or (row == piece.position[0]+2 and col == piece.position[1]-1) or (row == piece.position[0]+2 and col == piece.position[1]+1):
                if self.board.get_piece_at_position(row,col) is None or self.board.get_piece_at_position(row,col).color == 'white':
                    return True
        return False

    """
    This function checks if a move from the current
    position of a chess piece (passed as the piece
    parameter) to a new position on the board (specified
    by the row and col parameters) is a valid move for
    a bishop. It first checks if the move is diagonal
    and if the destination square is occupied by a
    piece of the same color. If these conditions are
    met, it then checks if there are any pieces in the
    path of the move by iterating through each square
    on the diagonal path between the current position
    and the destination square. If there is a piece on
    any of these squares, the function returns False,
    indicating that the move is not valid. If the move
    is valid, it returns True.
    """
    def is_valid_bishop_move(self, piece, row, col):
        from_row, from_col = piece.position
        if abs(row - from_row) != abs(col - from_col):
            return False
        if self.board.get_piece_at_position(row, col) is not None:
            if self.board.get_piece_at_position(row, col).color == piece.color:
                return False
        if from_row < row and from_col < col:
            for i in range(1, row - from_row):
                if self.board.get_piece_at_position(from_row + i, from_col + i) is not None:
                    return False
        elif from_row < row and from_col > col:
            for i in range(1, row - from_row):
                if self.board.get_piece_at_position(from_row + i, from_col - i) is not None:
                    return False
        elif from_row > row and from_col < col:
            for i in range(1, from_row - row):
                if self.board.get_piece_at_position(from_row - i, from_col + i) is not None:
                    return False
        elif from_row > row and from_col > col:
            for i in range(1, from_row - row):
                if self.board.get_piece_at_position(from_row - i, from_col - i) is not None:
                    return False
        return True

    """
    This method checks if a move made by a queen
    piece is valid. It first checks if the move
    is a valid rook move by calling the is_valid_rook_move
    function and passing the piece, row, and col as
    arguments. If the move is not a valid rook move,
    it then checks if the move is a valid bishop move
    by calling the is_valid_bishop_move function and
    passing the piece, row, and col as arguments. If
    either of these conditions are true, the move is
    considered valid and the function returns True.
    Otherwise, the move is considered invalid and the
    function returns False.
    """
    def is_valid_queen_move(self, piece, row, col):
        curr_row, curr_col = piece.position
        if (self.is_valid_rook_move(piece, row, col)) or (self.is_valid_bishop_move(piece, row, col)):
            return True
        else:
            return False

    """
    The method is_valid_king_move checks if a given move
    for the king piece is valid according to the rules
    of chess. It first checks if the move is only 1 space
    in any direction (horizontally or vertically) using
    the curr_row and curr_col variables which represent
    the current position of the king piece. If the move is
    one space in any direction, it then checks if the
    destination space is empty or occupied by an opposing
    piece's color. If the destination space is occupied
    by an opposing piece's color the move is valid and
    the function returns True. Next it checks if the king
    has moved before, if it has not moved, it checks if
    the move is a castling move and that the conditions
    for castling are met (the king and rook have not moved
    and the spaces between them are empty). If all the
    conditions are met the function returns true, if not
    the function returns false.
    """
    def is_valid_king_move(self, piece, row, col):
        curr_row, curr_col = piece.position
        if (abs(curr_row - row) <= 1 and abs(curr_col - col) <= 1):
            if self.board.get_piece_at_position(row, col) is not None:
                if piece.color == "white":
                    if self.board.get_piece_at_position(row, col).color == "black":
                        return True
                elif piece.color == "black":
                    if self.board.get_piece_at_position(row, col).color == "white":
                        return True
            else:
                return True
            return False
        elif piece.has_moved == False:
            if row == curr_row and col == curr_col+3 and self.board.get_piece_at_position(curr_row, curr_col+1) == None and self.board.get_piece_at_position(curr_row, curr_col+2) == None and self.board.get_piece_at_position(curr_row, curr_col+3).has_moved == False and self.board.get_piece_at_position(curr_row, curr_col+3).name == "rook" and self.board.get_piece_at_position(curr_row, curr_col+3).color == piece.color:
                return True
            elif row == curr_row and col == curr_col-4 and self.board.get_piece_at_position(curr_row, curr_col-1) == None and self.board.get_piece_at_position(curr_row, curr_col-2) == None and self.board.get_piece_at_position(curr_row, curr_col-3) == None and self.board.get_piece_at_position(curr_row, curr_col-4).has_moved == False and self.board.get_piece_at_position(curr_row, curr_col-4).name == "rook" and self.board.get_piece_at_position(curr_row, curr_col-4).color == piece.color:
                return True
        else:
            return False

    """

    """
    def is_in_check(self, color):
        king_position = self.find_king(color)
        if king_position is None:
            return False
        else:
            for row in range(8):
                for col in range(8):
                    piece = self.board.get_piece_at_position(row, col)
                    if piece is not None and piece.color != color:
                        if self.is_valid_move(piece, king_position[0], king_position[1]):
                            return True
            return False

    """
    This code is checking if a given color is in check.
    The function takes in a parameter "color" which
    represents the color of the king that needs to be
    checked for check. It first finds the position of
    the king on the board by calling the find_king()
    function and passing in the color of the king. If
    the king's position is not found, the function returns
    False. If the king's position is found, it then iterates
    through all the squares on the board, and for each
    piece that is not of the same color as the king, it
    checks if the move to the king's position is a valid move
    by calling the is_valid_move() function and passing in the
    piece, the row and column of the king's position. If any
    of these calls return true, the function returns true,
    indicating that the king is in check. Otherwise, it returns
    false, indicating that the king is not in check.
    """
    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        else:
            for row in range(8):
                for col in range(8):
                    piece = self.board.get_piece_at_position(row, col)
                    if piece is not None and piece.color == color:
                        for row2 in range(8):
                            for col2 in range(8):
                                if self.is_valid_move(piece, row2, col2):
                                    return False
            return True

    """
    This method is used to locate the position of the king on
    the chess board. It takes in a parameter "color" which can
    be either "white" or "black" and it represents the color of
    the king to be located. The function loops through the entire
    chess board by using nested loops, checking each position on
    the board. When it finds a piece at a position that is not
    None, it checks if the piece is a king and if it has the same
    color as the input parameter. If these conditions are met, the
    function returns a tuple containing the row and column of the
    king. If the king is not found, the function returns None.
    """
    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece_at_position(row, col)
                if piece is not None and piece.name == "king" and piece.color == color:
                    return (row, col)
        return None



def main():
    game = ChessGame()
    game.run()

if __name__ == "__main__":
    main()
