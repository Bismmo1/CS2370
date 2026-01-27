###CS 2370 labs.  
## Ollie Grazier

def print_checker_boundary_row():
    print("+-+-+-+-+-+-+-+-+")

def print_checker_boundary_column():
    print("| | | | | | | | |")
    
def print_checker_spaces_under_boundary():
    print("+-+-+-+-+-+-+-+-+")

def main():

    print_checker_boundary_row()
    print_checker_boundary_column()
    
for _ in range(4):
    main()
    
print_checker_spaces_under_boundary()
