#ocg1020.py
#Lab 8


#I made two lists, one of numbers, and another of words
numList = [1,5, 2, 3, 5, 6,]
strList = ['hello', 'friend', 'there', 'hello','bababooey', 'hello', 'there', 'hello', 'friend', 'what']
#Part 1
def get_sum(numList):
    total = 0#for this I created a total, then checked if i would be greater than the current number in total
    for i in range(len(numList)):
        total += numList[i]
        #print(total)
    
    return total
    
#Part 2
def sum_even(numList):
    totalEven = 0#first I checked if the num was even by % 2, if so then added it to totalEven
    for i in range(len(numList)):
        if numList[i] % 2 == 0:
            totalEven += numList[i]
            '''print(totalEven)
        else:
            print("Odd number, skipping", numList[i])'''
    
    return totalEven

#Part 3
def sum_odd(numList):
    totalOdd = 0#similar to sum_even, I simply swapped the if from == to !=, allowing it to check for non even numbers
    for i in range(len(numList)):
        if numList[i] % 2 != 0:
            totalOdd += numList[i]
            '''print(totalOdd)
        else:
            print("Even number, skipping", numList[i])'''
    
    return totalOdd

#Part 4
def get_max(numList):
    max = 0#For this one I compared the current number to the stored largest number in max, if it was larger the new number would take its place in max
    for i in range(len(numList)):
        if numList[i] > max:
            max = numList[i]
            '''print(max)
        else:
            print(numList[i] ,"is not larger than", max)'''
    return max

#Part 5
def CountWords(str):
    word_count = {}
    #I did this one a little different than the instructions and I hope this is okay. I used a string list instead of a string like in the example
    #I then check using an if statement if the word was added to a new dictonaryif so then it would add += 1 to the count of that word in the dictionary,
    #if not then it would add it to the dictionary and raise the count by 1. seen in the else: statement
    for word in str:
        if word in word_count:
            word_count[word] += 1
            
        else:
            word_count[word] = 1
    
    return word_count

#Part 6
def get_longest(strList):
    longest = ""
    for i in range(len(strList)):
        if len(strList[i]) > len(longest):
            longest = strList[i]
            '''print(longest)
        else:
            print(strList[i],  "is not longer than", longest)'''

    return longest
        



def main():
    
    
    print("Part 1: get_sum")
    print(get_sum(numList))
    print('======================')

    print("Part 2: sum_even")
    print(sum_even(numList))
    print('======================')

    print("Part 3: sum_odd")
    print(sum_odd(numList))
    print('======================')

    print("Part 4: get_max")
    print(get_max(numList))
    print('======================')

    print("Part 5: CountWords")
    print(CountWords(strList))
    print('======================')
    
    print("Part 6: get_longest")
    print(get_longest(strList))
    print('======================')

if __name__=='__main__':
    main()




