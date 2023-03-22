import datetime
from time import sleep
import math #to avoid spurious precision
import termcolor2
#https://www.geeksforgeeks.org/clear-screen-python/
import colorama
import os

global INITIAL
global FINAL

global DISTANCE

def getFormattedTime(minutes):
    if minutes <= 1:
        return "1 minute."
    elif minutes < 60:
        return str(minutes) + " minutes."
    else:
        hours = math.floor(minutes / 60)
        minutes = minutes % 60
        return str(hours) + " hours and " + str(minutes) + " minutes."

def printG(rows):
    for row in rows:
        print(' '.join(row))
        # print(row)
    print()

def makeRows(i,j,heights):
    # print("time")
    # print(getFormattedTime(461))
    global DISTANCE
    colorama.init()
    rows = []
    r = []
    for n in range(len(heights)):
        if i == -1 and j == n:
            r.append(termcolor2.colored('🬀 ', 'magenta'))
        else:
            # r.append("║N║")
            r.append(termcolor2.colored('╳ ', 'cyan'))
    rows.append(r)
    for n in range(8):
        row = []
        for n2 in range(len(heights)):
            if n == i and n2 == j:
                row.append(termcolor2.colored('█ ', 'yellow')) #change this to whatever color u want
            elif heights[n2] >= 8-n:
                row.append(termcolor2.colored('█ ', "green"))
                # row.append('█ ')
            else:
                row.append("  ")
        rows.append(row)
    # printG(rows)
    #took inspiration from one of my personal projects
    #https://github.com/bshah016/CS_Projects/blob/master/TTT.py
    print('\
 ╔════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦════╦════╗\t\n\
 ║ {0} ║ {1} ║ {2} ║ {3} ║ {4} ║ {5} ║ {6} ║ {7} ║ {8} ║ {9} ║ {10} ║ {11} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {12} ║ {13} ║ {14} ║ {15} ║ {16} ║ {17} ║ {18} ║ {19} ║ {20} ║ {21} ║ {22} ║ {23} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {24} ║ {25} ║ {26} ║ {27} ║ {28} ║ {29} ║ {30} ║ {31} ║ {32} ║ {33} ║ {34} ║ {35} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {36} ║ {37} ║ {38} ║ {39} ║ {40} ║ {41} ║ {42} ║ {43} ║ {44} ║ {45} ║ {46} ║ {47} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {48} ║ {49} ║ {50} ║ {51} ║ {52} ║ {53} ║ {54} ║ {55} ║ {56} ║ {57} ║ {58} ║ {59} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {60} ║ {61} ║ {62} ║ {63} ║ {64} ║ {65} ║ {66} ║ {67} ║ {68} ║ {69} ║ {70} ║ {71} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {72} ║ {73} ║ {74} ║ {75} ║ {76} ║ {77} ║ {78} ║ {79} ║ {80} ║ {81} ║ {82} ║ {83} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {84} ║ {85} ║ {86} ║ {87} ║ {88} ║ {89} ║ {90} ║ {91} ║ {92} ║ {93} ║ {94} ║ {95} ║\t\n\
 ╠════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣\t\n\
 ║ {96} ║ {97} ║ {98} ║ {99} ║ {100} ║ {101} ║ {102} ║ {103} ║ {104} ║ {105} ║ {106} ║ {107} ║\t\n\
 ╚════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩════╩════╝ \t'.format(
               rows[0][0], rows[0][1], rows[0][2], rows[0][3],rows[0][4], rows[0][5], rows[0][6], rows[0][7],rows[0][8], rows[0][9], rows[0][10], rows[0][11], 
               rows[1][0], rows[1][1], rows[1][2], rows[1][3],rows[1][4], rows[1][5], rows[1][6], rows[1][7],rows[1][8], rows[1][9], rows[1][10], rows[1][11], 
               rows[2][0], rows[2][1], rows[2][2], rows[2][3],rows[2][4], rows[2][5], rows[2][6], rows[2][7],rows[2][8], rows[2][9], rows[2][10], rows[2][11], 
               rows[3][0], rows[3][1], rows[3][2], rows[3][3],rows[3][4], rows[3][5], rows[3][6], rows[3][7],rows[3][8], rows[3][9], rows[3][10], rows[3][11], 
               rows[4][0], rows[4][1], rows[4][2], rows[4][3],rows[4][4], rows[4][5], rows[4][6], rows[4][7],rows[4][8], rows[4][9], rows[4][10], rows[4][11], 
               rows[5][0], rows[5][1], rows[5][2], rows[5][3],rows[5][4], rows[5][5], rows[5][6], rows[5][7],rows[5][8], rows[5][9], rows[5][10], rows[5][11], 
               rows[6][0], rows[6][1], rows[6][2], rows[6][3],rows[6][4], rows[6][5], rows[6][6], rows[6][7],rows[6][8], rows[6][9], rows[6][10], rows[6][11], 
               rows[7][0], rows[7][1], rows[7][2], rows[7][3],rows[7][4], rows[7][5], rows[7][6], rows[7][7],rows[7][8], rows[7][9], rows[7][10], rows[7][11],
               rows[8][0], rows[8][1], rows[8][2], rows[8][3],rows[8][4], rows[8][5], rows[8][6], rows[8][7],rows[8][8], rows[8][9], rows[8][10], rows[8][11]))
    print("Estimated time to completion is: " + getFormattedTime(DISTANCE))

def printGrid(i,j,k,l,heights):
    while 1:
        if k > i:
            for n in range(k-i+1):
                os.system('clear')
                makeRows(7-(i+n),j,heights)
                sleep(1.0)
            if l < j:
                for n2 in range(j-l):
                    os.system('clear')
                    makeRows(7-k,j-n2-1,heights)
                    sleep(1.0)
            else:
                for n2 in range(l-j):
                    os.system('clear')
                    makeRows(7-k,j+n2+1,heights)
                    sleep(1.0)
        else:
            if l < j:
                for n2 in range(j-l+1):
                    os.system('clear')
                    makeRows(7-i,j-n2,heights)
                    sleep(1.0)
            else:
                for n2 in range(l-j+1):
                    os.system('clear')
                    makeRows(7-i,j+n2,heights)
                    sleep(1.0)
            for n in range(i-k):
                os.system('clear')
                makeRows(7-(i-n-1),l,heights)
                sleep(1.0)
        key = input("Enter q to go to next step or any other key to repeat animation: ")
        if key == "q":
            break
        

def getCol(containers):
    smallest = [[0,0],999]
    for col in containers:
        if len(col) and col[0][1] < smallest[1]:
            smallest[0] = col[0][0]
            smallest[1] = col[0][1]
    if smallest[1] == 999:
        return 0
    return smallest

def getDistance(i,j,heights,containers):
    min_no_container = 1000
    no_container_ind = -1
    min_with_container = 1000
    container_ind = -1
    for ind in range(len(heights)):
        if ind != j and heights[ind] < 8:
            if len(containers[ind]) == 0:
                if abs(i-heights[ind]) + abs(j-ind) < min_no_container:
                    min_no_container = abs(i-heights[ind]) + abs(j-ind)
                    no_container_ind = ind
            else:
                if abs(i-heights[ind]) + abs(j-ind) < min_with_container:
                    min_with_container = abs(i-heights[ind]) + abs(j-ind)
                    container_ind = ind
    if min_no_container < 1000:
        return [min_no_container,no_container_ind]
    elif min_with_container < 1000:
        return [min_with_container,container_ind]
    moves_to_buffer = (8-i+j+4)
    return [moves_to_buffer,-1]

def getDistanceForBalance(i,j,heights,containers, left):
    if left: 
        min_no_container = 1000
        no_container_ind = -1
        min_with_container = 1000
        container_ind = -1
        for ind in range(len(heights)):
            if ind <= 6:
                if ind != j and heights[ind] < 8:
                    if len(containers[ind]) == 0:
                        if abs(i-heights[ind]) + abs(j-ind) < min_no_container:
                            min_no_container = abs(i-heights[ind]) + abs(j-ind)
                            no_container_ind = ind
                    else:
                        if abs(i-heights[ind]) + abs(j-ind) < min_with_container:
                            min_with_container = abs(i-heights[ind]) + abs(j-ind)
                            container_ind = ind
        if min_no_container < 1000:
            return [min_no_container,no_container_ind]
        elif min_with_container < 1000:
            return [min_with_container,container_ind]
        moves_to_buffer = (8-i+j+4)
        return [moves_to_buffer,-1]
    else:
        min_no_container = 1000
        no_container_ind = -1
        min_with_container = 1000
        container_ind = -1
        print("dist containers:")
        print(containers)
        length = len(heights)
        print("length: " + str(length))
        print(heights)
        # heights = heights[-6:]
        for ind in range(len(heights)):
            if ind >= 6:
                if heights[ind] < 8:
                    if len(containers[ind]) == 0:
                        if abs(i-heights[ind]) + abs(j-ind) < min_no_container:
                            print("yessirski2")
                            print("ind: " + str(ind))
                            print("heights: " + str(heights[ind]))
                            min_no_container = abs(i-heights[ind])
                            no_container_ind = ind
                    else:
                        if abs(i-heights[ind]) + abs(j-ind) < min_with_container:
                            min_with_container = abs(i-heights[ind]) + abs(j-ind)
                            container_ind = ind
        if min_no_container < 1000:
            print("ind bruh: " + str(no_container_ind))
            print(heights[no_container_ind])
            return [heights[no_container_ind],no_container_ind]
            # return [min_no_container,no_container_ind]
        elif min_with_container < 1000:
            return [min_with_container,container_ind]
        moves_to_buffer = (8-i+j+4)
        return [moves_to_buffer,-1]

def getClosestDistance(i,j,heights):
    mindist = 1000
    container_ind = -1
    for ind in range(len(heights)):
        if heights[ind] < 8:
            if abs(i-heights[ind]) + abs(j-ind) < mindist:
                mindist = abs(i-heights[ind]) + abs(j-ind)
                container_ind = ind
    return [mindist, container_ind]

def getClosestDistanceForBalance(i,j,heights,left):
    print(heights)
    if left:
        mindist = 1000
        container_ind = -1
        for ind in range(len(heights)):
            if heights[ind] < 8:
                if abs(i-heights[ind]) + abs(j-ind) < mindist:
                    mindist = abs(i-heights[ind]) + abs(j-ind)
                    container_ind = ind
        return [mindist, container_ind]
    else:
        mindist = 1000
        container_ind = -1
        for ind in range(len(heights)):
            if heights[ind] < 8:
                if abs(i-heights[ind]) + abs(j-ind) < mindist:
                    mindist = abs(i-heights[ind]) + abs(j-ind)
                    container_ind = ind
        return [mindist, container_ind]

def getMass(ship):
    left = 0
    right = 0
    for row in ship:
        for num in range(6):
            left += row[num][0]
            right += row[num+6][0]
    return [left,right]

def signin(first_name, last_name, log_file):
    print("Hello and welcome to Mr Keogh's shipping dock.")
    print("Enter your full name to sign in and start working")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    print("Welcome " + first_name + " " + last_name)
    print()
    log_file.write(str(datetime.datetime.now()) + " " + first_name + " " + last_name + " signs in\n")
    return [first_name, last_name]

def logoutoption(first_name, last_name, log_file):
    userselection = input("Enter s to logout\n or \nEnter t to log a comment\n or \nEnter any other key to continue to the next step: ")
    if userselection == "s":
        log_file.write(str(datetime.datetime.now()) + " " + first_name + " " + last_name + " signs out\n")
        return signin(first_name, last_name, log_file)
    elif userselection == "t":
        log_comment = input("Please enter the text you would like to log(Non reversible, if mistake, enter \"N/A\"): ")
        log_file.write(str(datetime.datetime.now()) + " " + first_name + " " + last_name + " logged: " + log_comment + "\n")
        return [first_name, last_name]
    else:
        return [first_name, last_name]
    
def manhattan(i,j,k,l):
    return abs(i - k) + abs(j - l)

def main():
    global DISTANCE
    log_file = open("logfile1.txt", "a")
    first_name = ""
    last_name = ""
    # signing in
    name = signin(first_name, last_name, log_file)
    first_name = name[0]
    last_name = name[1]

    # selecting manifest
    manifest_file_name = input("Please enter the manifest file name that you would like to open: ")
    container_count = 0
    file = open(manifest_file_name, "r")
    ship = [[],[],[],[],[],[],[],[]]
    for line in file:
        row = int(line[2:3])
        # col = int(line[4:6])
        weight = line[10:15].lstrip('0')
        if weight == "":
            weight = "0"
        else:
            container_count += 1
        name = line[18:].strip()
        ship[row-1].append([int(weight),name])
    file.close()
    log_file.write(str(datetime.datetime.now()) + " Manifest " + manifest_file_name + " is opened, there are " + str(container_count) + " containers on the ship\n")

    # for s in ship:
    #     print(s)

    # selecting task
    print("What would you like to do?")
    print("1. Offload containers from the ship onto the buffer or trucks")
    print("2. Balance the ship")
    selection = input()
    while selection != "1" and selection != "2":
        print("Invalid selection, please type 1 or 2")
        selection = input()

    # for offloading containers
    if(selection == "1"):
        container_freq = {}
        print("Once you are done with entering containers, enter q to quit")
        while(1):
            container_name = input("Please enter a container you would like to REMOVE from the ship: ")
            if(container_name == "q"):
                break
            elif container_name in container_freq:
                container_freq[container_name] += 1
            else:
                container_freq[container_name] = 1
        print()
        containers_to_load = []
        # print("Once you are done with entering containers, enter q to quit")
        while(1):
            container_name = input("Please enter a container you would like to LOAD onto the ship: ")
            if(container_name == "q"):
                break
            else:
                containers_to_load.append(container_name)
        # start A* with manhattan
        heights = [0,0,0,0,0,0,0,0,0,0,0,0]
        bufferheights = [0,0,0,0,0,0,0,0,0,0,0,0]
        for row in ship:
            for i in range(len(row)):
                if row[i][1] != "UNUSED":
                    heights[i] += 1
        containers = {}
        for i in range(len(ship)):
            for j in range(len(ship[i])):
                if ship[i][j][1] in container_freq:
                    if ship[i][j][1] in containers:
                        containers[ship[i][j][1]].append([[i,j],heights[j] - 1 - i,ship[i][j]])
                    else:
                        containers[ship[i][j][1]] = [[[i,j],heights[j] - 1 - i,ship[i][j]]]
        for container in containers:
            containers[container].sort(key=lambda x:x[1])
            while len(containers[container]) > container_freq[container]:
                containers[container].pop(container_freq[container])
        # print(containers)
        containers_by_col = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for container in containers:
            for elem in containers[container]:
                containers_by_col[elem[0][1]].append(elem)
        for col in containers_by_col:
            col.sort(key=lambda x:x[1])
            # print(col)


        total_distance = 0
        buffercount = 0
        lastrow = 8
        lastcol = 0
        smallest = getCol(containers_by_col)
        while smallest != 0:
            # print(smallest)
            # print(containers_by_col)
            for i in range(smallest[1]):
                dist = getDistance(heights[smallest[0][1]]-1,smallest[0][1],heights,containers_by_col)
                total_distance += dist[0]
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    # printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    heights[dist[1]] += 1
                else:
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = 8
                    lastcol = 0
                    # printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
                    dst = getClosestDistance(8,11,bufferheights)
                    total_distance += (dst*4) + 4
                    buffercount += 1
                # name = logoutoption(first_name, last_name, log_file)
                first_name = name[0]
                last_name = name[1]

                # print(heights)
            # print(smallest[0][0], smallest[0][1])
            # print("8 0")
            total_distance += (8-smallest[0][0]+smallest[0][1]) + 4
            for elem in containers_by_col[smallest[0][1]]:
                elem[1] -= (smallest[1] + 1)
                # print(elem)
            heights[smallest[0][1]] -= 1
            total_distance += manhattan(lastrow, lastcol, smallest[0][0], smallest[0][1])
            lastrow = 8
            lastcol = 0
            # printGrid(smallest[0][0],smallest[0][1],8,0,heights)
            # log_file.write(str(datetime.datetime.now()) + " " + containers_by_col[smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            # name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            total_distance += (dst[0]*2 + 8)
            # printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            # name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]

        # start onloading container process
        for i in range(len(containers_to_load)):
            dst = getClosestDistance(8,0,heights)
            total_distance += ((dst[0] + 2)*2)
            # printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            # log_file.write(str(datetime.datetime.now()) + " " + containers_to_load[i] + " container is onloaded\n")
            # name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        print("DISTANCE ESTIMATED: ", total_distance)
        DISTANCE = total_distance



        heights = [0,0,0,0,0,0,0,0,0,0,0,0]
        bufferheights = [0,0,0,0,0,0,0,0,0,0,0,0]
        for row in ship:
            for i in range(len(row)):
                if row[i][1] != "UNUSED":
                    heights[i] += 1
        containers = {}
        for i in range(len(ship)):
            for j in range(len(ship[i])):
                if ship[i][j][1] in container_freq:
                    if ship[i][j][1] in containers:
                        containers[ship[i][j][1]].append([[i,j],heights[j] - 1 - i,ship[i][j]])
                    else:
                        containers[ship[i][j][1]] = [[[i,j],heights[j] - 1 - i,ship[i][j]]]
        for container in containers:
            containers[container].sort(key=lambda x:x[1])
            while len(containers[container]) > container_freq[container]:
                containers[container].pop(container_freq[container])
        # print(containers)
        containers_by_col = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for container in containers:
            for elem in containers[container]:
                containers_by_col[elem[0][1]].append(elem)
        for col in containers_by_col:
            col.sort(key=lambda x:x[1])

        # start moving and offloading containers
        total_distance = 0
        buffercount = 0
        lastrow = 8
        lastcol = 0
        smallest = getCol(containers_by_col)
        while smallest != 0:
            # print(smallest)
            # print(containers_by_col)
            for i in range(smallest[1]):
                dist = getDistance(heights[smallest[0][1]]-1,smallest[0][1],heights,containers_by_col)
                total_distance += dist[0]
                DISTANCE -= dist[0]
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                d = 0
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    d = manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    heights[dist[1]] += 1
                else:
                    d = manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = 8
                    lastcol = 0
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
                    dst = getClosestDistance(8,11,bufferheights)
                    total_distance += (dst*4) + 4
                    buffercount += 1
                name = logoutoption(first_name, last_name, log_file)
                first_name = name[0]
                last_name = name[1]
                DISTANCE -= d

                # print(heights)
            # print(smallest[0][0], smallest[0][1])
            # print("8 0")
            d = (8-smallest[0][0]+smallest[0][1]) + 4
            for elem in containers_by_col[smallest[0][1]]:
                elem[1] -= (smallest[1] + 1)
                # print(elem)
            heights[smallest[0][1]] -= 1
            DISTANCE -= manhattan(lastrow, lastcol, smallest[0][0], smallest[0][1])
            lastrow = 8
            lastcol = 0
            printGrid(smallest[0][0],smallest[0][1],8,0,heights)
            log_file.write(str(datetime.datetime.now()) + " " + containers_by_col[smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
            DISTANCE -= d
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            d = (dst[0]*2 + 8)
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
            DISTANCE -= d

        # start onloading container process
        # containers_to_load = []
        # print("Once you are done with entering containers, enter q to quit")
        # while(1):
        #     container_name = input("Please enter a container you would like to load onto the ship: ")
        #     if(container_name == "q"):
        #         break
        #     else:
        #         containers_to_load.append(container_name)
        for i in range(len(containers_to_load)):
            dst = getClosestDistance(8,0,heights)
            DISTANCE -= 4
            # print(dst[0])
            # print(containers_to_load)
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            log_file.write(str(datetime.datetime.now()) + " " + containers_to_load[i] + " container is onloaded\n")
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
            DISTANCE -= (dst[0]*2)
        print("Specified ship containers have successfully been loaded and unloaded!")
        # print(heights)
        
        log_file.write(str(datetime.datetime.now()) + " Finished a Cycle. Manifest " + manifest_file_name + " was written to desktop, and a reminder popup to operator to send file was displayed")
        print("Please send the manifest file to the ship captain")





        
    # for balancing ship
    elif(selection == "2"):
        # start A*
        massList = []
        index_list = []
        masses = getMass(ship)
        balancemass = (masses[0] + masses[1])/2
        left = False
        if min(masses) == masses[0]:
            left = True
        # deficit = balancemass - masses[0]
        lowerbound_deficit = math.ceil((max(masses[0],masses[1]) - 0.9*min(masses[0],masses[1]))/1.9)
        # print(deficit)
        print(lowerbound_deficit)

        balanceScore = min(masses[0],masses[1])/max(masses[0],masses[1])
        print(balanceScore)
        # if (balanceScore < 0.9):
        # print('len of ship' + str(len(ship[0])))
        if left:
            for i in range(len(ship)):
                # print(ship[i]) HERE
                for j in range (7, 12):
                    containerdata = ship[i][j]
                    if containerdata[0] != 0:
                        massList.append(containerdata)
                        index_list.append([i, j])
        else:
            for i in range(len(ship)):
                # print(ship[i]) #HERE
                for j in range (0,7):
                    containerdata = ship[i][j]
                    if containerdata[0] != 0:
                        massList.append(containerdata)
                        index_list.append([i, j])
        # BOTH BELOW
        # print("masslists: ")
        # print(massList)
        # massList.sort(reverse=True)
        massList.sort(key=lambda x:x[0], reverse=True)
        # massList.sort(reverse=True)

        # print(massList) #THIS ONE
        containerstomove = {}
        for data in massList:
            if lowerbound_deficit == 0:
                break
            if data[0] <= lowerbound_deficit:
                containerstomove[data[1]] = 1
                lowerbound_deficit -= data[0]
        #ALL 3 Below
        # print("here") 
        # print(containerstomove)
        # print(lowerbound_deficit)

        heights = [0,0,0,0,0,0,0,0,0,0,0,0]
        bufferheights = [0,0,0,0,0,0,0,0,0,0,0,0]
        for row in ship:
            for i in range(len(row)):
                if row[i][1] != "UNUSED":
                    heights[i] += 1
        containers = {}
        for i in range(len(ship)):
            for j in range(len(ship[i])):
                if ship[i][j][1] in containerstomove:
                    if ship[i][j][1] in containers:
                        containers[ship[i][j][1]].append([[i,j],heights[j] - 1 - i])
                    else:
                        containers[ship[i][j][1]] = [[[i,j],heights[j] - 1 - i]]
        # print(containers) #THIS ONE
        for container in containers:
            containers[container].sort(key=lambda x:x[1])
            while len(containers[container]) > containerstomove[container]:
                containers[container].pop(containerstomove[container])
        # print(containers)
        containers_by_col = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for container in containers:
            for elem in containers[container]:
                containers_by_col[elem[0][1]].append(elem)
        for col in containers_by_col:
            col.sort(key=lambda x:x[1])


        #TO CALCULATE TIME TO COMPLETION
        # start moving and offloading containers
        total_distance = 0
        buffercount = 0
        lastrow = 8
        lastcol = 0
        smallest = getCol(containers_by_col)
        while smallest != 0:
            # print("smallest: ")
            # print(smallest)
            # print(containers_by_col)
            for i in range(smallest[1]):
                dist = getDistance(heights[smallest[0][1]]-1,smallest[0][1],heights,containers_by_col) #add back in a -1 to first param
                total_distance += dist[0]
                # print("bruh1: ")
                # print(dist[0])
                # print(total_distance)
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    # total_distance += manhattan(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1]) #DO WE EVEN NEED THIS IN HERE?
                    # print("bruh2: ")
                    # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                    # print(heights[dist[1]], dist[1])
                    # print(total_distance)
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    # print("here1")
                    # printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    heights[dist[1]] += 1
                else:
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    # print("bruh3: ")
                    # print(total_distance)
                    lastrow = 8
                    lastcol = 0
                    # print("here2")
                    # printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
                    dst = getClosestDistance(8,11,bufferheights)
                    total_distance += (dst*4) + 4
                    # print("bruh4: ")
                    # print(total_distance)
                    buffercount += 1
                # name = logoutoption(first_name, last_name, log_file)
                # first_name = name[0]
                # last_name = name[1]

                # print(heights)
            # print(smallest[0][0], smallest[0][1])
            # print("8 0")
            coord = [smallest[0][0], smallest[0][1]]
            # print("bool dawg")
            # print(left)
            dist = getDistanceForBalance(heights[smallest[0][0]],smallest[0][1],heights,containers_by_col, left) #delete the +1 if its messing up
            # print("dist")
            # print(dist)
            xcoord = dist[1]
            ycoord = dist[0]
            # print(dist[1])
            # print(dist[0])
            # print(smallest[0][0])
            # print(smallest[0][1])
            newcoords = manhattan(ycoord, xcoord, smallest[0][0], smallest[0][1])
            # print("newcoords")
            # print(newcoords)
            total_distance += newcoords #HERE AS WELL, this is to update the total distance
            # print("maybe here:")
            # print(newcoords)
            for elem in containers_by_col[smallest[0][1]]:
                elem[1] -= (smallest[1] + 1)
                # print(elem)
            heights[smallest[0][1]] -= 1
            # total_distance += manhattan(lastrow, lastcol, smallest[0][0], smallest[0][1])
            lastrow = 8
            lastcol = 0
            # print("here3")
            # printGrid(smallest[0][0],smallest[0][1], ycoord, xcoord, heights) #THIS LINE I THINK, this is to actually move it i think
            heights[dist[1]] += 1
            # print("Ship has been successfully balanced!")
            # print([smallest[0][1]])
            # log_file.write(str(datetime.datetime.now()) + " " + [smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            # name = logoutoption(first_name, last_name, log_file)
            # first_name = name[0]
            # last_name = name[1]
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            total_distance += (dst[0]*2 + 8)
            # print("here4")
            # printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            # name = logoutoption(first_name, last_name, log_file)
            # first_name = name[0]
            # last_name = name[1]
        

        # print("total time to completion: ")
        # print(total_distance)
        # return
        DISTANCE = total_distance
        heights = [0,0,0,0,0,0,0,0,0,0,0,0]
        bufferheights = [0,0,0,0,0,0,0,0,0,0,0,0]
        for row in ship:
            for i in range(len(row)):
                if row[i][1] != "UNUSED":
                    heights[i] += 1
        containers = {}
        for i in range(len(ship)):
            for j in range(len(ship[i])):
                if ship[i][j][1] in containerstomove:
                    if ship[i][j][1] in containers:
                        containers[ship[i][j][1]].append([[i,j],heights[j] - 1 - i])
                    else:
                        containers[ship[i][j][1]] = [[[i,j],heights[j] - 1 - i]]
        print(containers)
        for container in containers:
            containers[container].sort(key=lambda x:x[1])
            while len(containers[container]) > containerstomove[container]:
                containers[container].pop(containerstomove[container])
        # print(containers)
        containers_by_col = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for container in containers:
            for elem in containers[container]:
                containers_by_col[elem[0][1]].append(elem)
        for col in containers_by_col:
            col.sort(key=lambda x:x[1])
        
        #ACTUAL OUTPUT
        # start moving and offloading containers
        print("global dist: ")
        print(DISTANCE)
        total_distance = 0
        buffercount = 0
        lastrow = 8
        lastcol = 0
        smallest = getCol(containers_by_col)
        while smallest != 0:
            print("smallest: ")
            print(smallest)
            # print(containers_by_col)
            for i in range(smallest[1]):
                dist = getDistance(heights[smallest[0][1]]-1,smallest[0][1],heights,containers_by_col)
                total_distance += dist[0]
                print("homie: " + str(dist[0]))
                # DISTANCE -= dist[0]
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    move_dist = manhattan(heights[dist[1]], dist[1], smallest[0][0] + smallest[1] - i, smallest[0][1])
                    total_distance += move_dist
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    print("here1")
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    DISTANCE -= move_dist
                    heights[dist[1]] += 1
                else:
                    move_dist = manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    total_distance += move_dist
                    lastrow = 8
                    lastcol = 0
                    print("here2")
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
                    DISTANCE -= move_dist
                    dst = getClosestDistance(8,11,bufferheights)
                    total_distance += (dst*4) + 4
                    buffercount += 1
                name = logoutoption(first_name, last_name, log_file)
                first_name = name[0]
                last_name = name[1]

                # print(heights)
            print(smallest[0][0], smallest[0][1])
            # print("8 0")
            coord = [smallest[0][0], smallest[0][1]]
            print("bool dawg")
            print(left)
            dist = getDistanceForBalance(heights[smallest[0][0]],smallest[0][1],heights,containers_by_col, left) #delete the +1 if its messing up
            print("dist")
            print(dist)
            xcoord = dist[1]
            ycoord = dist[0]
            print(dist[1])
            print(dist[0])
            print(smallest[0][0])
            print(smallest[0][1])
            newcoords = manhattan(ycoord, xcoord, smallest[0][0], smallest[0][1])
            print("newcoords")
            print(newcoords)
            total_distance += newcoords #HERE AS WELL, this is to update the total distance
            for elem in containers_by_col[smallest[0][1]]:
                elem[1] -= (smallest[1] + 1)
                # print(elem)
            heights[smallest[0][1]] -= 1
            move_dist = manhattan(dist[0], dist[1], smallest[0][0], smallest[0][1])
            total_distance += move_dist
            lastrow = 8
            lastcol = 0
            print("here3")
            print(move_dist)
            printGrid(smallest[0][0],smallest[0][1], ycoord, xcoord, heights) #THIS LINE I THINK, this is to actually move it i think
            DISTANCE -= move_dist
            heights[dist[1]] += 1
            # print("Ship has been successfully balanced!")
            # print([smallest[0][1]])
            # log_file.write(str(datetime.datetime.now()) + " " + [smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        print("Ship has been successfully balanced!")
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            move_dist = (dst[0]*2 + 8)
            total_distance += move_dist
            print("here4")
            DISTANCE -= move_dist
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
    
    log_file.close()

if __name__ == "__main__":
    main()
