###CS 2370 labs.
## Ollie Grazier

def print_checker_boundary_row():
    print("+-+-+-+-+-+-+-+-+")

def print_checker_boundary_column():
    print("| | | | | | | | |")

def print_checker_spaces_under_boundary():
    print("+-+-+-+-+-+-+-+-+")
    
def draw_checker_board():
  for _ in range(4):
      print_checker_boundary_row()
      print_checker_boundary_column()

def main():

    print('Running the tests...')
    print() #empty line
    draw_checker_board()
    print_checker_spaces_under_boundary()

main()
print()
print("=-=-=-=-=-=-=-=-=")
print()

##checkerboard with pieces
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


draw_checker_board_with_pieces()
