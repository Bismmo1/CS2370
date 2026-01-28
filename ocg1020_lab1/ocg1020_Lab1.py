"""CS 2370 labs."""
"""Ollie Grazier"""
"""ocg1020@usnh.edu"""


##Part 1
print()
print("Part 1")
print("Hello, World!")

##Part 2
#1
print()
print("Part 2")
print('How mamny seconds are there in 42 minutes 42 seconds?')
minutes = 42
seconds = 42
## converting and combining the two
temp = (minutes * 60) 
total = temp + seconds 
print(total , "seconds")

#2
print('How many miles are there in 10 kilometers?')
kilometers = 10
## converting to miles
miles = kilometers * 1.6 
print(miles , "miles in 10 kilometers.")

#3
print("If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace per mile?, and what is your MPH?")
kilometers = 10
minutes = 42
seconds = 42
## converting to miles
miles = kilometers / 1.61


## converting and combining the two
timeSeconds = (minutes*60) + seconds 

## Finding how long to run 1 mile in min and sec
secondsPerMile = timeSeconds / miles

milesPerMinute = secondsPerMile//60
milesPerSecond = secondsPerMile%60

## Finding the mph
mph = 3600/secondsPerMile

print((int(milesPerMinute)) , "Minutes and" , (int(milesPerSecond)) , "Seconds per mile.")
print(round(mph, 1) , "mph")
print("mph is rounded, same with seconds to appear better.")


##Part 3
print()
print("Part 3")
coffee = "macchiatto"
print(coffee)

##Part 4
print()
print("Part 4")

cups_fry_needs = 100
cups_so_far = 6.5
print(cups_so_far >= cups_fry_needs)

##Part 5
#Creating a folder

##Part 6
#naming the file

##Part 7
#running the .py file from folder in cmd

##Part 8 
#defining main

##Part 9 & 11
##checker Board
def print_checker_boundary_row():
    print("+-+-+-+-+-+-+-+-+")

##Part 12
def print_checker_boundary_column():
    print("| | | | | | | | |")

##Part 13
#To print the rest of checkerboard I added a bottom/under boundary to print once more after loop stated in next def
def print_checker_spaces_under_boundary():
    print("+-+-+-+-+-+-+-+-+")
    
##Part 14
##Part 23

def draw_checker_board():
  for _ in range(8):
      print_checker_boundary_row()
      print_checker_boundary_column()

##Part24
#this was easy, just adding new functions I then called in intervals
#to replace the top and bottom, this can be viewed below
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

##Part 20
## Draughts Functions

def print_draughts_space_row():
  print("+-+-+-+-+-+-+-+-+-+-+")

def print_draughts_space_column():
  print("| | | | | | | | | | |")

def print_draughts_spaces_under_boundary():
  print("+-+-+-+-+-+-+-+-+-+-+")
  
##Part 22
## draughts board creation
def draw_draughts_board():
  for _ in range(10):
      print_draughts_space_row()
      print_draughts_space_column()
  print_draughts_spaces_under_boundary()

##Part 17 
#Creating Main function. It calls other functions stated above to minimize the size of main.
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

## Im not sure how this works but I will ask in class tomorrow (We will go over this soon.)
## Part 16
if __name__ == "__main__":
    main()
