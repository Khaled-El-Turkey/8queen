from random import randint

class nque:
    visited = []
    list_of_visits = []
    step = 0
def abs(a):
    if(a < 0):
        a = a*-1
    return a

def notInVisited(node):
    for i in range(len(nque.visited)):
        if node[0] == nque.visited[i][0] and node[1] == nque.visited[i][1]:
            return False
    return True


def print_Queens (q) :
    str =''
    for i in range(8) :
        for j in range(8):
            str +=' '+q[i][j]+ ' '
        str +='\n'

    print(str)


cost = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def set_cost(place):
    for i in range(8):
        u = (place[0]+i) % 8
        cost[u][place[1]] += 21
    for i in range(8):
        y = (place[1]+i) % 8
        if y != place[1]:
            cost[place[0]][y] += 21
    r = place[0]
    c = place[1]
    while r > 0 and c < 7:
        r -= 1
        c += 1
        if r != place[0] and c != place[1]:
            cost[r][c] += 21
    r = place[0]
    c = place[1]
    while c > 0 and r < 7:
        c -= 1
        r += 1
        if r != place[0] and c != place[1]:
            cost[r][c] += 21
    r = place[0]
    c = place[1]
    while r > 0 and c > 0:
        c -= 1
        r -= 1
        if r != place[0] and c != place[1]:
            cost[r][c] += 21
    r = place[0]
    c = place[1]
    while r < 7 and c < 7:
        c += 1
        r += 1
        if r != place[0] and c != place[1]:
            cost[r][c] += 21


def reset_cost(place):
    for i in range(8):
        u = ((place[0] + i) % 8)
        cost[u][place[1]] -= 21
    for i in range(8):
        y = ((place[1] + i) % 8)
        if y != place[1]:
            cost[place[0]][y] -= 21
    r = place[0]
    c = place[1]
    while r > 0 and c < 7:
        r -= 1
        c += 1
        if r != place[0] and c != place[1]:
            cost[r][c] -= 21
    r = place[0]
    c = place[1]
    while c > 0 and r < 7:
        c -= 1
        r += 1
        if r != place[0] and c != place[1]:
            cost[r][c] -= 21
    r = place[0]
    c = place[1]
    while r > 0 and c > 0:
        c -= 1
        r -= 1
        if r != place[0] and c != place[1]:
            cost[r][c] -= 21
    r = place[0]
    c = place[1]
    while r < 7 and c < 7:
        c += 1
        r += 1
        if r != place[0] and c != place[1]:
            cost[r][c] -= 21
        ''' for i in range(8):
                for j in range(8):
                    if (abs(i-j) == abs(place[0]-place[1]))or (i+j == place[0]+place[1]):
                        cost[i][j] -= 21'''

possible_places = []

def Gheuristic(costs):
    G = 0
    for i in range(8):
        for j in range(8):
            if costs[i][j]==0:
                G+=1
    return G

def get_possible_for_col():
    posc = []
    for i in range(8):
        for j in range(8):
            if cost[i][j] == 0:
               posc.append([i, j, 0])
    return posc


def sort_pos(pos):
        for i in range(0, len(pos)):
            for j in range(i, len(pos)):
                if pos[j][2] <= pos[i][2]:
                    tmp = pos[i]
                    pos[i] = pos[j]
                    pos[j] = tmp
        return pos

def getpossso(pos):
    for i in range(len(pos)):
        compute_heuristics(pos[i], i,pos)
    pos = sort_pos(pos)
    return pos

def compute_heuristics(possible_pos, ind,pos):
    set_cost(possible_pos)
    g = Gheuristic(cost)
    pos[ind][2] = g
    reset_cost(possible_pos)

queen_pos=[]
noOfNONAqueen=0
nqueen=[
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0']
]

rowav=[0,1,2,3,4,5,6,7]

print("the initial state is :")
print("-----------------------------")
print_Queens(nqueen)
print("-----------------------------")

posqueenr = 0
posqueenc =0

def getSequence(noOfNONAqueen):
    possible_places = getpossso(get_possible_for_col())
    nque.step = 0
    while possible_places:
        node = possible_places[-1]
        e = notInVisited(node)
        while e and((node[2] + noOfNONAqueen) >= 7) and noOfNONAqueen < 8:
            nque.step += 1
            possible_places.pop(-1)
            nque.visited.append(node)
            set_cost(node)
            noOfNONAqueen += 1
            if noOfNONAqueen >= 8:
                break
            children = getpossso(get_possible_for_col())
            if len(children) <= 0:
                reset_cost(nque.visited[-1])
                item1 = nque.visited[-1]
                nque.visited.pop(-1)
                if len(nque.visited) > 0:
                    item2 = nque.visited[-1]
                else:
                    break
                orphans = getpossso(get_possible_for_col())
                if item1 == orphans[0]:
                    reset_cost(nque.visited[-1])
                    nque.visited.pop(-1)
                    noOfNONAqueen -= 1
                noOfNONAqueen -= 1
            else:
                possible_places.extend(children)
            node = possible_places[-1]
            e = notInVisited(node)
        if noOfNONAqueen >= 8:
            break
        elif node[2] + noOfNONAqueen < 7:
            children = getpossso(get_possible_for_col())
            for i in range(len(children)):
                if children[i] in possible_places:
                    possible_places.remove(children[i])
            reset_cost(nque.visited[-1])
            item1 = nque.visited[-1]
            nque.visited.pop(-1)
            if len(nque.visited) > 0:
                item2 = nque.visited[-1]
            else:
                break
            orphans = getpossso(get_possible_for_col())
            if item1 == orphans[0]:
                reset_cost(nque.visited[-1])
                nque.visited.pop(-1)
                noOfNONAqueen -= 1
            noOfNONAqueen -= 1
        elif not e:
            possible_places.pop(-1)
        elif len(nque.visited) <= 0:
            break
    if len(nque.visited) == 8:
        return nque.visited
    else:
        return [False]

def solve(noOfNONAqueen=0, posqueenr = 0, posqueenc =0):
    posqueenr = randint(0, 7)
    posqueenc = randint(0, 7)
    nque.visited = [[posqueenr, posqueenc, -1]]
    set_cost([posqueenr, posqueenc, -1])
    noOfNONAqueen += 1
    listr = getSequence(noOfNONAqueen)
    if len(listr) == 8:
        for i in range(len(listr)):
            nqueen[listr[i][0]][listr[i][1]] = '1'
            print("after step " + str(i+1) + " :")
            print("-----------------------------")
            print_Queens(nqueen)
            print("-----------------------------")
        print("the number of steps of searching is "+str(nque.step))
        return False
    else:
        nque.visited = []
        return True

def tot():
    d = solve(0)
    while d == True:
        d = solve(0)
tot()

