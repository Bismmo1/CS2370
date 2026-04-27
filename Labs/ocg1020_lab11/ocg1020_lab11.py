#ocg1020_lab11.py


#Part 1: Check pdf attached

        
#Part 2: RPS
def readgame(txt):
    listA=[]#Define lists for players
    listB=[]

    #Winner variables
    a = 0
    b = 0
    
    f = open(txt,'r')#read specified file
    games_played = f.readline()#take in number of games played
    rounds = int(games_played)#Convert number of games played to integer
    hands = f.readline()#read the hands played
    
    f.close()#Close File
    
    #print(games_played)
    #print(hands)
    #print(len(hands))

    #Break readline hands into player A and B
    for i in range(len(hands)):
        if i % 2 == 0:#start with player A, using len to determine hands
            #print("A",hands[i])
            listA.append(hands[i])#append i to player a list
        else:
            #print("B",hands[i])
            listB.append(hands[i])
    #print(listA,listB)
    


    #Logic
    #R > S
    #S > P
    #P > R


    #Create or check for a file with winning scores named output.txt
    output = open("output.txt","w")
    
    for i in range(rounds):
        output.write(f"Game: {i+1} ")
    
        if listA[i] == 'R':#Rock Condition
            if listB[i] == 'S':#Check for win
                output.write(f'A Wins, {listA[i]} beats {listB[i]} \n')
                a += 1#add to score
                
            elif listB[i] == 'R':#Check for tie
                output.write(f'Tie, {listA[i]} same as {listB[i]} \n')
                
            else:#else you lost
                output.write(f'B Wins, {listB[i]} beats {listA[i]} \n')
                b += 1#add to score
        elif listA[i] == "S":#Scissors Condition
            if listB[i] == "P":
                output.write(f'A Wins, {listA[i]} beats {listB[i]} \n')
                a += 1
                
            elif listB[i] == 'S':
                output.write(f'Tie, {listA[i]} same as {listB[i]} \n')
                
            else:
                output.write(f'B Wins, {listB[i]} beats {listA[i]} \n')
                b += 1

        elif listA[i] == "P":#Paper Condition
            if listB[i] == "R":
                output.write(f'A Wins, {listA[i]} beats {listB[i]} \n')
                a += 1
                
            elif listB[i] == 'P':
                output.write(f'Tie, {listA[i]} same as {listB[i]} \n')
                
            else:
                output.write(f'B Wins, {listB[i]} beats {listA[i]} \n')
                b += 1

        else:
            output.write(f"something is wrong... {listA[i]} {listB[i]} \n")#Conditional for improper format/ errors

    if a > b:#compare and find the winner
        output.write("A Wins the Game!")
    elif a == b:
        output.write(" Its a Tie!")

    else:
         output.write("B Wins the Game!")
    
    output.close()


#Part 3: WordCount
def WordCount(input_file, output_file):
    word_count = {}
    
    # 1. Open and read the input file to count words
    with open(input_file, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    
    #open output file and print the results
    f = open(output_file, 'w')
        # Sorts so its easier to read (saw this while looking for ways to print this nicely)
    for word in sorted(word_count.keys()):
        f.write(f"{word}: {word_count[word]}\n")


    f.close()
    return word_count  #Return Final Dictionary
        



print(WordCount("midsummer.txt","midsummerCount.txt"))
