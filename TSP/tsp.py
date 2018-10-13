from collections import defaultdict

city = defaultdict(list)
cost = defaultdict(list)

def addEdge(city,u,v,weight):
    city[u].append(v)
    cost[u].append(weight)
    
def generateEdges(city):
    edges = [] 
    for node in city:
        for neighbour in city[node]:
            edges.append((node,neighbour))
    
    return edges

ch = input('Do you want to use pre-generated city?: ')

if(ch=='n'):
    ch='y'
    while(ch!='n'):
        node1 = input('Enter first node: ')
        node2 = input('Enter second node: ')
        addEdge(city,node1,node2,wt)
        ch = input('Do you want to enter more edges?: ')

else:
    addEdge(city,'d','a',8) 
    addEdge(city,'a','b',9)
    addEdge(city,'a','d',8) 
    addEdge(city,'b','c',0) 
    addEdge(city,'b','a',9) 
    addEdge(city,'c','d',3) 
    addEdge(city,'c','b',0)  
    addEdge(city,'d','c',3) 
    ###
    # addEdge(city,'a','c',3)
    # addEdge(city,'a','g',1)
    # addEdge(city,'a','d',0)
    # addEdge(city,'c','a',3)
    # addEdge(city,'c','x',5)
    # addEdge(city,'x','c',5)
    # addEdge(city,'x','p',8)
    # addEdge(city,'x','l',5)
    # addEdge(city,'l','x',5)
    # addEdge(city,'l','e',7)
    # addEdge(city,'p','x',8)
    # addEdge(city,'p','f',1)
    # addEdge(city,'p','e',0)
    # addEdge(city,'f','p',1)
    # addEdge(city,'f','d',3)
    # addEdge(city,'f','b',6)
    # addEdge(city,'d','f',3)
    # addEdge(city,'d','a',0)
    # addEdge(city,'d','g',7)
    # addEdge(city,'g','d',7)
    # addEdge(city,'g','a',1)
    # addEdge(city,'g','b',0)
    # addEdge(city,'b','g',0)
    # addEdge(city,'b','f',6)
    # addEdge(city,'b','e',6)
    # addEdge(city,'e','p',0)
    # addEdge(city,'e','b',6)
    # addEdge(city,'e','l',7)

paths= ["a"]
penalty = [0]

def find_all_paths(city,paths):
    temp_paths = paths[:]
    for i in range(len(temp_paths)):
        l = len(temp_paths[i])
        node = temp_paths[i][l-1]
        flag=0
        for neighbour in city[node]:
            if neighbour not in temp_paths[i]:
                if(flag==0):
                    x = temp_paths[i]
                    x+=neighbour
                    temp_paths[i]=x
                    flag=1
                    penalty[i]+=cost[node][city[node].index(neighbour)]
                else:
                    x = paths[i]
                    x+=neighbour
                    temp_paths.append(x)
                    penalty.append(cost[node][city[node].index(neighbour)])
    paths = temp_paths[:]
    return paths

i=110
while(i>0):
    paths = find_all_paths(city,paths)
    i-=1

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))
            
node="a" #Start point

cycles=[]
calc_cost=[]
penalty1 = []



for path in dfs(city,node,node):
    if(len(path)>2):
        cycles.append("".join([node]+path))
        calc_cost.append([node]+path)

min = penalty[0]
j = 0
for i in range(1,len(penalty)):
    if(penalty[i]<min):
        min=penalty[i]
        j=i

def find_cost(i,list,penalty1):
    penalty1.append(0)
    for j in range(len(list)-1):
        penalty1[i]+=cost[list[j]][city[list[j]].index(list[j+1])]


for i in range(len(calc_cost)):
    find_cost(i,calc_cost[i],penalty1)

print('Min cost path is: %d th' % j)
print(paths[j])
print(penalty)

print(penalty1)

min = penalty1[0]
j = 0
for i in range(1,len(penalty1)):
    if(penalty1[i]<min):
        min=penalty1[i]
        j=i

print('Min cost path is: %d th' % j)
print(cycles[j])
