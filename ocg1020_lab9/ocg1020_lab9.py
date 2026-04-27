#ocg1020_lab9

#Part 1
def even_characters_only(string):
    print("Part 1 A: even characters only")
    stored = ""#temp for the even characters
    for x in string: #repeat for the entire string
        if ord(x) % 2 == 0:  #check for even chacter
             stored += x#sored if even
    return(stored)
#Part 1.2
def odd_characters_only(string):
    print("Part 1 B:odd characters only")
    temp = ""#temp for the odd characters
    for x in string:#repeat for entire string
        if ord(x) % 2 != 0:  #check if NOT even
            temp += x#store if odd
    return(temp)

#Part 2
def merge_strings(a,b):
    print("Part 2: merge strings")
    left = "" #temp for left string
    right = "" #temp for right string
    if len(a) == len(b):#if equal, default to A
        #print("Both are same length, I will print A first then B.")
        return "".join([a, b])#prints a first
        
    elif len(a) > len(b):# 
        #print("A is larger")
        mid = len(a) // 2
        return "".join([a[:mid], b, a[mid:]])#prints a first
    else:
        #print("B is larger")
        mid = len(b) // 2
        return "".join([b[:mid], a, b[mid:]])#prints b first

    
#Part 3
def reverse_strings_a(string):#no library
    print("Part 3 A: No library")
    return(string[::-1])#simply reverses the string using slicing

def reverse_strings_b(string):#with library
    print("Part 3 B: with library")
    temp = list(string)#turns string into a list
    temp.reverse()#reverses the list
    return("".join(temp))#combines the list into a string
    
#Part 4
def no_spaces_a(string):#no library
    print("Part 4 A: without library")
    result = ""
    for x in string:
        if x != " ":
            result += x
    print(result)
    print()
    
def no_spaces_b(string):#with library
    print("Part 4 B: with library")
    return string.replace(" ","")#replaces all spaces with nothing

#Part 5
def reverse_sentence_a(string):#with library
    print("Part 5 A: with library")
    reverse = (string.split(" "))#split into a list
    
    reverse = reverse[::-1]#reverse the list
    
    return " ".join(reverse)#combine the list into one string
    
def reverse_sentence_b(string):#no library
    print("Part 5 B: no library")
    words=[]
    temp=""#temp for each word
    for x in string:
        if x == " ":#add temp word when space is reached
            words.append(temp)#add temp to list
            temp=""
        else:
            temp += x#add character to temp
    if temp:
        words.append(temp)#add last word to list if there is one

    reversed_sentence=""
    for i in range(len(words)-1,-1,-1):
        #starts at -1, loops to -1, and will step back by -1 until finished
        reversed_sentence += words[i]#add the word to the reversed sentence
        if i > 0:
            reversed_sentence +=" "#add space

    return reversed_sentence

    
#Part 6
def repeat_string(string,times):
    
    if times <= 0:
        return ""
    return string + repeat_string(string, times - 1)#recursive
    #returns string x times

    
#Part 7
def first_characters(string,times):
    print("Part 7: First characters")
    return (string[:times])#print the first x characters, where x is the number of times
    

#Part 8
def reverse_second_words():
    print("Part 8:reverse second words")
    sentence = str(input("Enter a sentence: "))#user input
    words = sentence.split()#split the sentence into a list of words
    for i in range(len(words)):#loop through the list of words
        if i % 2 == 1:#if odd, reverse the word
            words[i] = words[i][::-1]#reverse by slicing
    return(" ".join(words))#combine the list into a string then print

#Part 9
def rotate_word(string, amount):
    print("Part 9: rotate word")
    result = []#temp for the result
    shift = amount % 26# if its greater than 26(bc chr consists of more than just the alphabet)
    for ch in string:
        if 'a' <= ch <= 'z':#if lowercase, rotate within lowercase range
            base = ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))#rotate by shifting x characters
        elif 'A' <= ch <= 'Z':#if uppercase, rotate within uppercase range
            base = ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))#rotate by shifting x characters
        else:
            result.append(ch)#if not a letter, just add it to the result without rotating
    return ''.join(result)#return the result as a str


def main():
    #you can change these strings for the tests

    #Part 1
    #Part 7
    string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #Part 2
    string2 = "small world"
    string3 = "big worldsss"
    #Part 3
    string4 = "Hello"
    #Part 4
    string5 = "hi there happy owl!"
    #Part 5
    string6 = "the sky is blue"
    #Part 6
    #Part 7
    string7 = "hello"
    times = 5

    #Part 1
    print(even_characters_only("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print()
    print(odd_characters_only("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print()

    #Part 2
    print(merge_strings("small world", "big world"))
    print()

    #Part 3
    print(reverse_strings_a("Hello"))
    print()
    print(reverse_strings_b("Hello"))
    print()


    #Part 4
    no_spaces_a("hi there happy owl!")
    print(no_spaces_b("hi there happy owl!"))
    print()

    #Part 5
    print(reverse_sentence_a("the sky is blue"))
    print()
    print(reverse_sentence_b("the sky is blue"))
    print()

    #Part 6
    print("Part 6: repeat string")#This haad to be here because of the recursive function, otherwise it would print every time the function is called
    print(repeat_string("hello", 5))
    print()

    #Part 7
    print(first_characters("ABCDEFG", 5))
    print()

    #Part 8
    print(reverse_second_words())
    print()

    #Part 9
    print(rotate_word("cheer", 7))
    print()
    print(rotate_word("melon", -10))
    print()

if __name__=="__main__":
    main()
