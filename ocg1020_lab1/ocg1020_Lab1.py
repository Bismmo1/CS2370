"""CS 2370 labs."""
"""Ollie Grazier"""


##checker Board
def print_checker_boundary_row():
    print("+-+-+-+-+-+-+-+-+")

def print_checker_boundary_column():
    print("| | | | | | | | |")

def print_checker_spaces_under_boundary():
    print("+-+-+-+-+-+-+-+-+")
    
def draw_checker_board():
  for _ in range(8):
      print_checker_boundary_row()
      print_checker_boundary_column()


##checkerboard pieces
def checker_x_0():
  print("+-+-+-+-+-+-+-+-+")
  print("|x| |x| |x| |x| |")

def checker_x_1():
  print("+-+-+-+-+-+-+-+-+")
  print("| |x| |x| |x| |x|")

def checker_o_0():
  print("+-+-+-+-+-+-+-+-+")
  print("|o| |o| |o| |o| |")

def checker_o_1():
  print("+-+-+-+-+-+-+-+-+")
  print("| |o| |o| |o| |o|")

#create checkerboard with pieces
def draw_checker_board_with_pieces():
  checker_x_1()
  checker_x_0()
  checker_x_1()
  for _ in range(2):
      print_checker_boundary_row()
      print_checker_boundary_column()
  checker_o_0()
  checker_o_1()
  checker_o_0()

## Draughts Functions

def print_draughts_space_row():
  print("+-+-+-+-+-+-+-+-+-+-+")

def print_draughts_space_column():
  print("| | | | | | | | | | |")

def print_draughts_spaces_under_boundary():
  print("+-+-+-+-+-+-+-+-+-+-+")
  
## draughts board creation
def draw_draughts_board():
  for _ in range(10):
      print_draughts_space_row()
      print_draughts_space_column()
  print_draughts_spaces_under_boundary()

def main():

    print('Running the tests...')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()
    ##draw Checkerboard
    draw_checker_board()
    print_checker_spaces_under_boundary()
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()
    ##draw the checkerboard with pieces
    draw_checker_board_with_pieces()
    print_checker_spaces_under_boundary()
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()
    ##draw the draughts board
    draw_draughts_board()
    print_draughts_spaces_under_boundary()

## Im not sure how this works but I will ask in class tomorrow
if __name__ == "__main__":
    main()
