import datetime
from time import sleep
import math #to avoid spurious precision

def printG(rows):
    for row in rows:
        print(row)
    print()

def makeRows(i,j,heights):
    rows = []
    r = []
    for n in range(len(heights)):
        if i == -1 and j == n:
            r.append("O")
        else:
            r.append("N")
    rows.append(r)
    for n in range(8):
        row = []
        for n2 in range(len(heights)):
            if n == i and n2 == j:
                row.append("O")
            elif heights[n2] >= 8-n:
                row.append("X")
            else:
                row.append(" ")
        rows.append(row)
    printG(rows)

def printGrid(i,j,k,l,heights):
    while 1:
        if k > i:
            for n in range(k-i+1):
                makeRows(7-(i+n),j,heights)
                sleep(2.0)
            if l < j:
                for n2 in range(j-l):
                    makeRows(7-k,j-n2-1,heights)
                    sleep(2.0)
            else:
                for n2 in range(l-j):
                    makeRows(7-k,j+n2+1,heights)
                    sleep(2.0)
        else:
            if l < j:
                for n2 in range(j-l+1):
                    makeRows(7-i,j-n2,heights)
                    sleep(2.0)
            else:
                for n2 in range(l-j+1):
                    makeRows(7-i,j+n2,heights)
                    sleep(2.0)
            for n in range(i-k):
                makeRows(7-(i-n-1),l,heights)
                sleep(2.0)
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
    userselection = input("Enter s to logout or any other key to continue to the next step: ")
    if userselection == "s":
        log_file.write(str(datetime.datetime.now()) + " " + first_name + " " + last_name + " signs out\n")
        return signin(first_name, last_name, log_file)
    else:
        return [first_name, last_name]
    
def manhattan(i,j,k,l):
    return abs(i - k) + abs(j - l)

def main():
    log_file = open("logfile1.txt", "w")
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
            container_name = input("Please enter a container you would like to remove from the ship: ")
            if(container_name == "q"):
                break
            elif container_name in container_freq:
                container_freq[container_name] += 1
            else:
                container_freq[container_name] = 1
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
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    heights[dist[1]] += 1
                else:
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = 8
                    lastcol = 0
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
                    dst = getClosestDistance(8,11,bufferheights)
                    total_distance += (dst*4) + 4
                    buffercount += 1
                name = logoutoption(first_name, last_name, log_file)
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
            printGrid(smallest[0][0],smallest[0][1],8,0,heights)
            log_file.write(str(datetime.datetime.now()) + " " + containers_by_col[smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            total_distance += (dst[0]*2 + 8)
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]

        # start onloading container process
        containers_to_load = []
        print("Once you are done with entering containers, enter q to quit")
        while(1):
            container_name = input("Please enter a container you would like to load onto the ship: ")
            if(container_name == "q"):
                break
            else:
                containers_to_load.append(container_name)
        for i in range(len(containers_to_load)):
            dst = getClosestDistance(8,0,heights)
            total_distance += ((dst[0] + 2)*2)
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            log_file.write(str(datetime.datetime.now()) + " " + containers_to_load[i] + " container is onloaded\n")
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        print("total number of minutes moving containers is: ", total_distance)
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
                print(ship[i])
                for j in range (7, 12):
                    containerdata = ship[i][j]
                    if containerdata[0] != 0:
                        massList.append(containerdata)
                        index_list.append([i, j])
        else:
            for i in range(len(ship)):
                print(ship[i])
                for j in range (0,7):
                    containerdata = ship[i][j]
                    if containerdata[0] != 0:
                        massList.append(containerdata)
                        index_list.append([i, j])

        print("masslists: ")
        print(massList)
        # massList.sort(reverse=True)
        massList.sort(key=lambda x:x[0], reverse=True)
        # massList.sort(reverse=True)

        print(massList)
        containerstomove = {}
        for data in massList:
            if lowerbound_deficit == 0:
                break
            if data[0] <= lowerbound_deficit:
                containerstomove[data[1]] = 1
                lowerbound_deficit -= data[0]
        print("here")
        print(containerstomove)
        print(lowerbound_deficit)

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
        
        # start moving and offloading containers
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
                # print(smallest[0][0] + smallest[1] - i, smallest[0][1])
                heights[smallest[0][1]] -= 1
                if dist[1] != -1:
                    # print(heights[dist[1]], dist[1])
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = heights[dist[1]]
                    lastcol = dist[1]
                    print("here1")
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1],heights[dist[1]], dist[1], heights)
                    heights[dist[1]] += 1
                else:
                    total_distance += manhattan(lastrow, lastcol, smallest[0][0] + smallest[1] - i, smallest[0][1])
                    lastrow = 8
                    lastcol = 0
                    print("here2")
                    printGrid(smallest[0][0] + smallest[1] - i, smallest[0][1], 8, 0, heights)
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
            total_distance += manhattan(lastrow, lastcol, smallest[0][0], smallest[0][1])
            lastrow = 8
            lastcol = 0
            print("here3")
            printGrid(smallest[0][0],smallest[0][1], ycoord, xcoord, heights) #THIS LINE I THINK, this is to actually move it i think
            heights[dist[1]] += 1
            # print([smallest[0][1]])
            # log_file.write(str(datetime.datetime.now()) + " " + [smallest[0][1]][0][2][1] + " container is offloaded\n")
            # print(heights)
            # print(total_distance)
            containers_by_col[smallest[0][1]].pop(0)
            smallest = getCol(containers_by_col)  
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
        for i in range(buffercount):
            dst = getClosestDistance(8,0,heights)
            total_distance += (dst[0]*2 + 8)
            print("here4")
            printGrid(8,0,heights[dst[1]],dst[1],heights)
            heights[dst[1]] += 1
            name = logoutoption(first_name, last_name, log_file)
            first_name = name[0]
            last_name = name[1]
    
    log_file.close()

if __name__ == "__main__":
    main()
