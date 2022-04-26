#smakes and ladders
#https://www.geeksforgeeks.org/snake-ladder-problem-2/

#Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from source or 1st cell. Basically, the player has total control over outcome of dice throw and wants to find out minimum number of throws required to reach last cell.

# If the player reaches a cell which is base of a ladder, the player has to climb up that ladder and if reaches a cell is mouth of the snake, has to go down to the tail of snake without a dice throw.

#-----------


# why graph problem
    #we can only transition on 1 direction
    # if you move up, no gaurenteed path back to where you came from

    #neighots of 0? what you can get to in 1 dice roll and directed edges

# what kind of traversal
    #shortest path, BFS

# what extensions
    #get neighbors again is different
    #rolling 1-6 also check for snakes and ladders
    # keep track of len of shortest path

# code it up
    # do we need to build adj list? No next 6 numbers are neighbors

    #mutiple traversal?
        #if we dont reach in 1 traversal? it means start and end are not connected
        #another traversal wouldnt help, hit cycle most likely

        #will there be a case where I go through a square twice

    #extension
        #rolling dice to get neighbors
        #keep track of shortest len so far

def snakes_ladders(n, s_l):

    #O(n) -> time/space

    #start at 0

    #1D array instead of 2D

    #s_l = [0, 1, 15, 3, 4, 5, 6, 7, 36] # input example

    #s_l[where i rolled]= where I land

    distance = [-1] * (n+1) # how many dice rolls away each node is from 0

    distance[0] = 0 # 0 is starting poing

    #other options is to create a tuple queue
    #queue.append((0, 0))
    #would need visited array in tuple approach
    queue = [0]

    while queue:
        curr = queue.pop(0)
        for neighbor in range(curr+1, min(curr+7, n+1)): #out of bounds provision
            landed = s_l[neighbor]
            if distance[landed] == -1:
                #queue.append(landed, distance+1)
                queue.append(landed)
                distance[landed] = distance[curr] + 1 # 1 dice roll away from 0
                #looking for goal: n
                if landed == n:
                    return distance[n]

    return -1
