#ocg1020_lab7.py

#Part1
def p_square(rows):
    for i in range(rows):
        #Simple problem we went over in class with numbers, converted it to chr.
        print((chr(65+i)+" ")*(rows), end="")
        print()

#Part2
def LTriangle(row):
    for i in range(row):
        #I spent so long trying to make this work just to add another space at the beginning, crazy
        #simple addition of a row after each loop and subtraction of a space. Looped for (row) number of times
        print("  "*(row-i-1)+(chr(65+i)+" ")*(i + 1), end="")
        print()

#Part3
def RTriangle(row):
    for i in range(row+1):
        #Had to split the row subtraction into a main loop, and create a "sub loop"
        #to print the characters
        print(" "*(i-row),end="")
        for j in range(0,row-i):
            print(chr(65+j),end=" ")
        print()
#Part4
def numPyramid(row):
    #This is not the best looking, but it works really well
    #I couldnt find a neater way to do this, it just looks like too much code for what it does
    for i in range(row+1):#first we add to the stack
        print(end="")
        for j in range(1,i+1):
            print((row-j),end=" ")
        print()
    for i in range(row,0,-1):#Then we subtract from the stack
        print(end="")
        for j in range(1,i):
            print((row-j),end=" ")
        print()

#Part5
def Triangle(row):
    for i in range(row+1):#Defining how many times it will stack
        print(" "*(i),end="")
        for j in range(0,row-i):#Subtracting i from range to reduce number of loops
            print(int(row-i-j),end=" ")#Subtracting i and j to get acheived result
        print()

#Part6
def Diamond(row): #Its pretty muc the exact same as Part 5 I just stacked two of them
    #and one is in reverse order
    for i in range(row+1):
        print(" "*(row-i),end="")
        for j in range(0,i):
            print(int(j+1),end=" ")
        print()
    for i in range(row-1,0,-1):
        print(" "*(row-i),end="")
        for j in range(0,i):
            print(int(j+1),end=" ")
        print()




#Part 7
def hollowDiamond(n):
    #Im not sure if this is exactly whast you were looking for, my results
    #look slightly different than yours. I belive this is jusit due to font/format
    
    # Top half of the diamond
    for i in range(1, n + 1):
        if i == 1:
            # First row only has one star
            print(" " * (n - i) + "*")
            #printing our given, by the range to get pattern
        else:
            #two stars with spaces in between
            #I found this to be the best way to solve this, while attempting to solve this i thought a complex algorithm could
            #do it all in one line. instead i just made an if else and it worked.
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
            
    # Bottom half of the diamond
    for i in range(n, 0, -1):
        if i == 1:
            # Last row only has one star
            print(" " * (n - i) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")



#Part 8
#I was challenged by this one, the best method I found was to make
#the center equal to the number of stars given. this allowed both even and odd inputs from the user,
#its not identical to your arrow but im happy with this solution. with some more guidance of exacts that you were looking for,
#like for the neck to be equal to half the given number i couldve been a bit more specific with this one. I was unsure what you were looking for
def arrow(n):
    # Arrow head
    for i in range(1, n + 1):
        # Print spaces nd stars separated by space
        print("  " * (n - i) + "* " * (2 * i - 1))
        
    #Neck of arrow
    for i in range(n+1):
        #n is +1 to match your photo
        # Calculate spaces to center a 3-star wide stem under the triangle
        print("  " * (n - 2) + "* " * 3)

def main():

   s = 5
   #you can modify them all at once with this variable. 

   print("Part 1")
   print()
   p_square(s)
   print()
   
   print("Part 2")
   print()
   LTriangle(s)
   print()
   
   print("Part 3")
   print()
   RTriangle(s)
   print()
   
   print("Part 4")
   print()
   numPyramid(s)
   print()
   
   print("Part 5")
   print()
   Triangle(s)
   print()
   
   print("Part 6")
   print()
   Diamond(s)
   print()
   
   print("Part 7")
   print()
   hollowDiamond(s)
   print()
   
   print("Part 8")
   print()
   arrow(s)
   print()

if __name__ == "__main__":
    main()
