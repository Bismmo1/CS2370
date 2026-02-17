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
    
    
def main():
    #Part1
    print("Part 1")
    print(is_triangle(3, 7, 5))
    print()
    
    #Part2
    print("Part 2")
    print(print_whether_right_triangle(3, 4, 5))
    print()
    


if __name__ == "__main__":
    main()