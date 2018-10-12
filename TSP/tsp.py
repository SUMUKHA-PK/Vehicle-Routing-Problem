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
    while(ch=='y'):
        node1 = input('Enter first node: ')
        node2 = input('Enter second node: ')
        addEdge(city,node1,node2)
        ch = input('Do you want to enter more edges?: ')

else:
    addEdge(city,'a','c') 
    addEdge(city,'b','c') 
    addEdge(city,'b','e') 
    addEdge(city,'c','d') 
    addEdge(city,'c','e') 
    addEdge(city,'c','a') 
    addEdge(city,'c','b') 
    addEdge(city,'e','b') 
    addEdge(city,'d','c') 
    addEdge(city,'e','c') 

paths= ["a"]
def find_all_paths(city,paths,num,node):
    