#Game of Tic-tac-toe
"""
TODO: 
add win/lose condition
change size of a board

"""

from random import randint

print "Welcome to game of Tic-tac-toe!"
print ""

player_symbol = raw_input("Enter your player_symbol, X or O: ").upper()
opponent_symbol = ""
while player_symbol != "X" and player_symbol != "O":
  player_symbol = raw_input("Symbol should be X or O: ").upper()
if player_symbol == "X":
  opponent_symbol = "O"
else:
  opponent_symbol = "X"
print "Your opponent chose", opponent_symbol

board = []
for i in range(0, 3):
  board.append(["-"] * 3)

def rows_cols_numbering():
  print "Rows and Columns are numbered from 1 to 3."
  numbering_question = str(raw_input("Do you want to have them numbered? (Y/N)"))
  if numbering_question.upper() == "Y":
    return True
  else:
    return False
    
numbering = rows_cols_numbering()

def draw_board(board):
  if numbering == True:
    print "Numbering"
    """
    print " " + "|".join(range(3)) + "|"
    """
    for row in board:
      print "|" + "|".join(row) + "|"


  elif numbering == False:
    for row in board:
      print "|" + "|".join(row) + "|"
  print ""



draw_board(board)

def main_game():
  for turn in range(5):
    print "----TURN %s----" %(turn + 1)

    #Player's move
    valid_move = False 
    while valid_move == False: #Repeats until player makes a valid move
      player_row = raw_input("Enter your row:    ")
      player_col = raw_input("Enter your column: ")

      if player_row.isdigit() == False or player_col.isdigit() == False: #Enforces numerical input
        print "You should enter a natural number.\n"

      else:
        player_row = int(player_row)
        player_col = int(player_col)

        if player_row - 1 not in range(3):                 #Move off the board
          print "Your move should be on the board.\n"
        elif board[player_row - 1][player_col - 1] != "-": #Move in a written tile
          print "This tile is already taken.\n"
        elif board[player_row - 1][player_col - 1] == "-": #Is a valid move
          valid_move = True
        else:                                              #Unsuspected error
           print "Something went wrong.\n"


    board[player_row - 1][player_col - 1] = player_symbol
    draw_board(board)
  
    #Allows opponent to move only if tile is empty and there are moves left
    if turn < 4:
      opponent_row = randint(1, 3)
      opponent_col = randint(1, 3)
      while board[opponent_row - 1][opponent_col - 1] != "-":
        opponent_row = randint(1, 3)
        opponent_col = randint(1, 3)
      board[opponent_row - 1][opponent_col - 1] = opponent_symbol
      print "Opponent's move:"
    else:
      print "Game over! I guess you won. Your opponent has run out of moves."
      break

    draw_board(board)

    turn += 1
  
main_game()


