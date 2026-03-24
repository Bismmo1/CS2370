#ocg1020_lab5


#Part1
def partial_countdown(count,step):
    count += 1

    #Check if number is greater than 10 and if it will be greater after next subtraction
    while(10 < count and 10 < count - step):
        count = count - step
        print(count)
    #Subtract 1 once you are about to hit 10 and stop at 1
    while(count > 1):
        
        count-=1
        print(count)
    else:
        print("Blastoff!")

#Part2
def print_first_n_multiples(n, num_multiples):
    #define a multiplier counter
    mult = 0
    for i in range(num_multiples):
        #create a temp to print out
        temp = n * mult
        #add to mult count
        mult = mult + 1
        print(temp, end = ' ')

#Part3
def print_whether_n_looks_indivisble(n, x):
    #check if indivisible first
    if x < 2:
        print(f"{n} looks like it's indivisible for the given range.")
        return
    #then find greatest divisible factor
    if n % x == 0:
        print(f"{n} is divisible by {x} .")
        return
    else:
        print_whether_n_looks_indivisble(n, x - 1)
        
#Part4
def power_of(x,n):
    print(x**n)

#Part5
def count_digits(n):
    #start a count, this will keep track of how many times we loop
    count = 0
    #if the int is 0, then add 1 so it counts as one digit
    if n == 0:
        count += 1
    temp = n
    #check if we are above 0, if so add one to count, and divide by 10 to remove one digit
    while temp > 0:
        count += 1
        temp //= 10
    print(count)

def main():

    #Part 1
    print("Part 1, partial_countdown")
    count = int(input("Enter a integer for your count:"))
    step = int(input("Enter a integer for your step:"))
    partial_countdown(count, step)
    print()

    #Part2
    print("Part 2, print_first_n_multiples")
    n = int(input("Enter a integer for your number to be multiplied:"))
    num_multiples = int(input("Enter a integer for number of times multiplied:"))
    print_first_n_multiples(n, num_multiples)
    print()

    #Part3
    print("Part3, print_whether_n_looks_indivisble")
    x = int(input("Enter your number:"))
    y = int(input("Enter your Factor:"))
    print_whether_n_looks_indivisble(x, y)
    print()

    #Part4
    print("Part4, power_of")
    x = int(input("Enter your Number:"))
    y = int(input("Enter your Exponent:"))
    power_of(x, y)
    print()

    #Part5
    print("Part5, count_digits")
    n = int(input("Enter your number to find out how many digits:"))
    count_digits(n)
    
if __name__ == "__main__":
    main()
