#ocg1020_lab6

#Part1
def gcd(x,y):
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    while y:
        #swap x and y, and set y to the remainder of x divided by y
        x, y = y, x % y
    return x    


#Part2
def reverseDigits(n):
    rev = 0
    while n > 0:
        #add reversed number to the end of the current reversed number
        rev = rev * 10 + n % 10
        #remove the last digit from n
        n = n // 10
        #loop until n is 0, at which point rev will be the reversed number
    return rev

#Part3
def fibonacci(n):
    a, b = 0, 1
    #print the first n Fibonacci numbers
    for _ in range(n):
        print(a, end=' ')
        #update a and b to the next two Fibonacci numbers
        a, b = b, a + b

#Part4
def factorial(n):
    #We just did this in class the other day
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
#Part5
def summation(start, stop):
    total = 0
    #Pretty much the same as the add(n) we just did in class
    while start <= stop:
        total += start
        start += 1
    return total

#part6
def perfectNumber(n):
    #begin loop to find the sum of the proper divisors of n
    while n > 0:
        total = 0
        for i in range(1, n):
            #if i is a proper divisor of n, add it to the total
            if n % i == 0:
                total += i
        return total == n
    
#Part7
def gotMoney():
    money = 0

def main():


    #Part 1
    '''print("Part 1: GCD Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("GCD of", x, "and", y, "is", gcd(x, y))
    print()

    #Part 2
    print("Part 2: Reverse Digits")
    n = int(input("Enter a number: "))
    print("Reversed number is:", reverseDigits(n))
    print()

    #Part 3
    print("Part 3: Fibonacci Sequence")
    n = int(input("Enter the number of Fibonacci terms to display: "))
    fibonacci(n)
    print()

    #Part 4
    print("Part 4: Factorial Calculator")
    n = int(input("Enter a number: "))
    print("Factorial of", n, "is", factorial(n))
    print()

    #Part 5
    print("Part 5: Summation Calculator")
    start = int(input("Enter the starting number: "))
    stop = int(input("Enter the stopping number: "))
    print("Summation from", start, "to", stop, "is", summation(start, stop))

    #Part 6
    print("Part 6: Perfect Number Checker")
    n = int(input("Enter a number: "))
    if perfectNumber(n):
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")'''
    
    #Part 7
    print("Part 7: Got Money?")
    gotMoney()


main()
