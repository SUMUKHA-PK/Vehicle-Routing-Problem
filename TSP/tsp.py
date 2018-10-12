from collections import defaultdict

city = defaultdict(list)

def addEdge(city,u,v):
    city[u].append(v)

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
        addEdge(city,node1,node2)
        ch = input('Do you want to enter more edges?: ')

else:
    addEdge(city,'a','b')
    addEdge(city,'a','d') 
    addEdge(city,'b','c') 
    addEdge(city,'b','a') 
    addEdge(city,'c','d') 
    addEdge(city,'c','b')  
    addEdge(city,'d','c') 
    addEdge(city,'d','a') 

paths= ["a"]

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
                else:
                    x = paths[i]
                    x+=neighbour
                    temp_paths.append(x)
    paths = temp_paths[:]
    return paths

i=110
while(i>0):
    paths = find_all_paths(city,paths)
    i-=1

print(paths)
