##ocg1020
##Lab 2 CS2370
import math

pi = math.pi
##Part 1 ; 10 points
def volumeOfSphere():
    r = float(input("Enter Sphere Radius: "))
    volume = (4/3) * pi * (math.pow(r,3))
    print("Volume of sphere is", volume, type(volume))

##Part 2 ; 10 points
def print_total_wholesale_cost():
    cover_price = float(input('Price of book: '))
    number_of_copies = int(input('Number of copies you will purchase: '))

    ## calculate the 40% off
    discounted_price = cover_price * .6

    ## caclulate the shipping
    if number_of_copies <= 0:
        return 0.0
    elif number_of_copies == 1:
        return 3.0
    else:
        first_copy_cost = 3.0
        additional_copies = number_of_copies - 1
        additional_cost = additional_copies * 0.75
        total_cost = first_copy_cost + additional_cost + (discounted_price * number_of_copies)
    
    ## returning answer
    print('your total for books will be: $', total_cost, type(total_cost))

##Part 3
def distanceTravelled():

    #user inputs
    print("Part 3, Enter parameters to find disntace travelled.")
    velocity = float(input('Velocity (m/s): '))
    acceleration = float(input('Acceleration (m/s): '))
    time = float(input('Time (seconds): '))
    
    #getting distance
    distance = (velocity*time) + (1/2 * acceleration * (time**2))

    print("Distance: ", distance , type(distance))

##Part 4
def bmiCalculator():
    masskg = float(input('Weight (kg): '))
    heightm = float(input('Height (meters): '))

    ## calculate bmi
    bmi = masskg / (heightm **2)
    print("Your BMI is: ", bmi, type(bmi))

##Part 5 
def areaOfPrism():
    length = float(input('Length: '))
    width = float(input('Width: '))
    height = float(input("Height: "))
    surface_area = 2 * ((length * 2) * (width * 2) * (height * 2))
    print("the surface area is ", surface_area, type(surface_area))

def main():
    '''Runs tests for all functions.'''
    print('Lab 2 Tests:') #Add new ones here\
     ##Part 0
    width = 17
    height = 12.0
    delimiter = '5'
    print('Part 0')
    print("width/2:         ", width/2, "  Data type: ", type(width/2))
    print("width/2.0:       ",width/2.0, "  Data type: ", type(width/2.0))
    print("width%2:         ",width % 2, "    Data type: ", type(width%2))
    print("width // 2:      ",width // 2, "    Data type: ", type(width//2))
    print("height/3:        ",height/3 , "  Data type: ", type(height/3))
    print("height**2:       ",height**2 , "Data type: ", type(height**2))
    print("1 + 2 *5:        ",1 + 2 *5 , "   Data type: ", type(1 + 2 *5))
    print("delimiter * 5:   ",delimiter * 5 , "Data type: ", type(delimiter * 5))
    print("delimiter + '5': ",delimiter + '5', "   Data type: ", type(delimiter + '5'))
    print()
    
    ##Part 1
    print('Part 1')
    volumeOfSphere()
    print()

    ##Part 2
    print('Part 2')
    print_total_wholesale_cost()
    print()

    ##part 3
    print('Part 3')
    distanceTravelled()
    print()

    ##part 4
    print('Part 4')
    bmiCalculator()
    print()

    ##part 5
    print('Part 5')
    areaOfPrism()

main()
