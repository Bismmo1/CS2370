#ocg1020_lab10.py

import random#for part 4

class Car:
    '''
    Creates a Car with the Specified Parameters

    @param: color, defines color
    @param: pos, defines position of the car (an integer)
    @param: speed, defines car’s speed 
    '''


    #Part 0
    def __init__(self, color, start_pos, speed):
        #Assign Variables
        self.color = color #define color
        self.speed = speed #define speed it travels at
        self.start_pos = start_pos #define starting position
        self.pos = start_pos #define the updating position


    #Part 1 and 2
    def drive(self, time, direction):
        #print(self.color,f"car will drive {direction} for {time} hours.")#Debug code
        
        if direction == "forward":#Checks for forward direction
            distance = time * self.speed#finds the distance travelled
            self.pos += distance#adds the distance travelled to position
            
        elif direction == "backward":#Checks for backward direction
            distance = time * self.speed#finds the distance travelled
            self.pos -= distance#subtracts the distance(moved backwards)
            
        #print(self.color,f"car is now at {self.pos}.")#debug code

    
    #Part 3
    def __str__(self):
        if self.pos == self.start_pos:
            return(f"The {self.color} car is back at starting position {self.pos}")
        else:
            return(f"The {self.color} car is currently at position {self.pos}")

    
            
    

myCar = Car('brown',2, 3) 
print(myCar)
myCar.drive(3, 'forward')
print(myCar)
myCar.drive(2, 'backward') 
print(myCar)


def race():
    laps = int(input("Enter Number of Laps to complete: "))
    
    # Store cars in a list for easy iteration
    cars = [
        Car("Red", 0, 1),
        Car("Blue", 0, 1),
        Car("Green", 0, 1),
        Car("Yellow", 0, 1)
    ]

    for lap in range(laps):#Create x amount of laps
        print(f"Lap{lap}!")#Call new lap
        
        for car in cars:
            direction = 'forward' if random.randint(0, 1) == 0 else 'backward'#update direction
    
            distance = random.randint(0, 20) #Randomize speed
    
            car.drive(distance, direction)#assign distance and direction
    
            print(f"{car.color} car moved {direction}. New position: {car.pos}")#print message for car color, direction and position
        
    winner_car = cars[0]#make new variable and assign the first car to it

    for i in range(1, len(cars)):
        current_contender = cars[i]#make a new variable for contender
        
        # Compare their pos
        if current_contender.pos > winner_car.pos:
            # If this cars position is higher, its the new winner
            winner_car = current_contender#assign new winner
    return (f"The {winner_car.color} car has won! In place {winner_car.pos}")#return the winner
    

print(race())

