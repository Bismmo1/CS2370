# ollie_grazier_lab4.py


# Part1
def is_triangle(x, y, z):
    if (x + y > z) and (x + z > y) and (y + z > x):
        return True
    else:
        return False
    
#Part2
def print_whether_right_triangle(x, y, z):
    if not is_triangle(x, y, z):
        print(f"A right triangle cannot have sides of length {x}, {y}, and {z}.")
        return
    #pythagorean theorem : I used this wikipedia page to help me with the math as i forgot it.
    #https://en.wikipedia.org/wiki/Pythagorean_theorem
    if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (y**2 + z**2 == x**2):
        print(f"A right triangle can have sides of length {x}, {y}, and {z}.")
    else:
        print(f"A right triangle cannot have sides of length {x}, {y}, and {z}.")
    
#Part3
def check_is_square():
    x1 = int(input("Enter x1 for Bottom Left: "))
    y1 = int(input("Enter y1 for Bottom Left: "))
    x2 = int(input("Enter x2 for Bottom Right: "))
    y2 = int(input("Enter y2 for Bottom Right: "))
    x3 = int(input("Enter x3 for Top Left: "))
    y3 = int(input("Enter y3 for Top Left: "))
    x4 = int(input("Enter x4 for Top Right: "))
    y4 = int(input("Enter y4 for Top Right: "))

    def get_distance(xa, ya, xb, yb):
        return (xb - xa)**2 + (yb - ya)**2
    side1 = get_distance(x1, y1, x2, y2) # p1 to p2 (Bottom)
    side2 = get_distance(x2, y2, x4, y4) # p2 to p4 (Right)
    side3 = get_distance(x4, y4, x3, y3) # p4 to p3 (Top)
    side4 = get_distance(x3, y3, x1, y1) # p3 to p1 (Left)
    
    if side1 > 0 and side1 == side2 == side3 == side4:
        print("Yes – it is a Square")
    else:
        print("No – it is not a square")\
            
# Part4
def conversation(s):
    if s == "bye":
        print("Have a nice day!")
    else:
        print(f"Did you say {s} ?")
        next_input = input()

        conversation(next_input)
        
#Part5
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
        
def main():
    '''x = float(input("Enter length for side x: "))
    y = float(input("Enter length for side y: "))
    z = float(input("Enter length for side z: "))
    print()
    
    # Part 1
    if is_triangle(x, y, z):
        print(f"A triangle can have sides of length {x}, {y}, and {z}.")
    else:
        print(f"A triangle cannot have sides of length {x}, {y}, and {z}.")
    print()
    
    # Part 2
    print_whether_right_triangle(x, y, z)
    print()
    
    #Part 3
    check_is_square()
    
    #Part 4
    first_s = input("Start the conversation: ")
    conversation(first_s)
    print()
    
    #Part5
    user_input = int(input("Enter an integer to cascade: "))
    cascade(user_input)'''
    
    #Part6
    

if __name__ == "__main__":
    main()