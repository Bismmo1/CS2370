#ocg1020.py
#Lab 8



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
            #I created else statements for testing almost all functions, these can be uncommented
            #You can see logical explainations
            '''print(totalEven)'''
        else:
            '''print("Odd number, skipping", numList[i])'''
            pass
    
    return totalEven

#Part 3
def sum_odd(numList):
    totalOdd = 0#similar to sum_even, I simply swapped the if from == to !=, allowing it to check for non even numbers

    for i in range(len(numList)):
        if numList[i] % 2 != 0:
            totalOdd += numList[i]
            '''print(totalOdd)'''
        else:
            '''print("Even number, skipping", numList[i])'''
            pass
    
    return totalOdd

#Part 4
def get_max(numList):
    max = 0#For this one I compared the current number to the stored largest number in max, if it was larger the new number would take its place in max

    for i in range(len(numList)):
        if numList[i] > max:
            max = numList[i]
            '''print(max)'''
        else:
            '''print(numList[i] ,"is not larger than", max)'''
            pass
    return max

#Part 5
def CountWords(string):
    #create a temp dictionary, this will eventually hold all your words and counts
    word_count = {}
    temp = string.split()#you can split a string into a list using this
    #print(temp)
    
    for word in temp:#read each word in list temp, then compare it to word_count
        if word in word_count:
            word_count[word] += 1#add a count to that specific word
            
        else:
            #print("storing", word)
            word_count[word] = 1#if it does not exist make a new word in word_count

    #Uncomment for another way to print this list
    '''for a, b in word_count.items():
        print(f"{a}: {b}", end=" ")#This way we print each part of the dictionary one at a time.
        
    '''
    return word_count#return the completed dictionary


'''def CountWords_ocg1020_version(strList):
    word_count = {}#this is the same as above, except it skips past converting a string into a list
    
    for word in string:
        if word in word_count:
            word_count[word] += 1
                
        else:
            word_count[word] = 1
            
        
    return word_count'''



#Part 6
def get_longest(strList):
    longest = ""#placeholder/temp

    for i in range(len(strList)):
        if len(strList[i]) > len(longest):#compare current to longest
            longest = strList[i]
            '''print(longest)'''
        else:
            '''print(strList[i],  "is not longer than", longest)'''
            pass

    return longest#return longest
        



def main():

    #Lists
    numList = [1,5, 2, 3, 5, 6,]
    list2 = "hello yes there hello hello yes friend yes hello"


    #list for personal def version of part 5
    strList = ['hello', 'friend', 'there', 'hello','bababooey', 'hello', 'there', 'hello', 'friend', 'what']
        
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
    print(CountWords(list2))
    print('======================')
    

    print("Part 6: get_longest")
    print(get_longest(strList))
    print('======================')

if __name__=='__main__':
    main()




