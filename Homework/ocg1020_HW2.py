#ocg1020_HW2

#Part 1: get_sums
def get_sums(a):
    final = []#create final list
    for i in a:#read through list
        sum_of = 0#create sum_of to store total
        for x in i:#loop for each list in the list
            sum_of += x#add to get total

        final.append(sum_of)#add sum_of as a new item in the list
    return final#return final list


#Part 2
def index_of_max_in_range(numbers,low_index,high_index):
    max_index = low_index#Set first value
    for i in range(low_index, high_index):#loops for specified range in list
        if numbers[i] > numbers[max_index]:#compares current number [i] to max index so far
            
            max_index = i#replace max index
            
    return max_index


#Part 3
def swap_elements(array,index_a, index_b):
    #temporary variable
    temp = array[index_a]
    #move from b to a
    array[index_a] = array[index_b]
    #move back into b from temp
    array[index_b] = temp
    return array#return swapped list


#Part 4
def selection_sort(numbers):
    n = len(numbers)
    # Iterate through each position in the list
    for i in range(n):
        max_idx = index_of_max_in_range(numbers, i, n)
        
        # If the max element is not already at the current position 'i', swap them.
        if max_idx != i:
            swap_elements(numbers, i, max_idx)#swaps using my other function
    return numbers


#Part 5
def rotate_list(numList, k):
    n = len(numList)#Gets list Length
    # Normalize k to be within the range [0, n-1]
    effective_k = k % n
    # Create a new list to hold the result
    rotated = [0] * n
    # Loop through the original list and place elements in their new positions
    for i in range(n):
        
        # Calculate the new index
        # If rotating right by k, element at i moves to (i + k)
        new_index = (i + effective_k) % n
        rotated[new_index] = numList[i]
        
    return rotated


def main():
    #Part 1
    list_of_lists = [[1, 2, 3], [4, 5], [10]]
    print("#Part 1: Sum of sublists")
    print(get_sums(list_of_lists))
    print()

    #part 2
    nums_part2 = [10, 15, 1, 20, 40]
    print("#Part 2: Index of max in range")
    print(index_of_max_in_range(nums_part2, 0, 4))
    print()

    #Part 3
    nums_part3 = [10, 15, 1, 20, 40]
    print("#Part 3: Swap elements")
    print(swap_elements(nums_part3, 1, 3))
    print()

    #Part 4
    nums_part4 = [10, 15, 1, 20, 40]
    print("#Part 4: Selection Sort")
    print(selection_sort(nums_part4))
    print()

    #Part 5
    nums_part5 = [1, 2, 3, 4, 5, 6]
    print("#Part 5: Rotate list by 2 (Right)")
    print(rotate_list(nums_part5, 2))
    
    print("#Part 5: Rotate list by -2 (Left)")
    print(rotate_list(nums_part5, -2))
    print()

if __name__ == "__main__":
    main()
