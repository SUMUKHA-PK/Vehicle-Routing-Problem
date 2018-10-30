from collections import defaultdict
import time
import numpy as np
import itertools
import sys

start = time.time()

city = defaultdict(list)
weights = defaultdict(list)

def addEdge(city,u,v,weight):
    city[u].append(v)
    weights[u].append(weight)
    
def generateEdges(city):
    edges = [] 
    for node in city:
        for neighbour in city[node]:
            edges.append((node,neighbour))
    
    return edges

def findsubsets(S,m):
    listing = [list(x) for x in itertools.combinations(S, m)]
    return listing


ch = input('Do you want to use pre-generated city?: ')

if(ch=='n'):
    flag_source = 0
    ch='y'
    while(ch!='n'):
        node1 = input('Enter first node: ')
        if(flag_source==0):
            print("First node entered will be set as source node: ")
            source_node = node1
            flag_source = 1
        node2 = input('Enter second node: ')
        addEdge(city,node1,node2,wt)
        ch = input('Do you want to enter more edges?: ')

else:

    # a----------9---------b
    # |                    |
    # |                    |
    # |                    |
    # 8                    0
    # |                    |
    # |                    |
    # |                    |
    # d----------3---------c

    # addEdge(city,'d','a',8) 
    # addEdge(city,'a','b',9)
    # addEdge(city,'a','d',8) 
    # addEdge(city,'b','c',0) 
    # addEdge(city,'b','a',9) 
    # addEdge(city,'c','d',3) 
    # addEdge(city,'c','b',0)  
    # addEdge(city,'d','c',3) 
    # source_node = 'a'
   
    ###

    # Graph for below
    #     c-----3-----a----------1
    #    /             \          \
    #   5               0          \
    #  /                 \          \
    # x                   d-----7----g
    # |\                 /           / 
    # | 8               3           0
    # |  \             /           /
    # |   p-----1-----f-----6-----b
    # |    \                     / 
    # |     \                   / 
    # |      \                 / 
    # |       \               /
    # 5        0             6
    # |         \           / 
    # |          \         / 
    # |           \       /
    # |            \     /
    # |             \   /
    # l-------7-------e

    addEdge(city,'a','c',3)
    addEdge(city,'a','g',1)
    addEdge(city,'a','d',0)
    addEdge(city,'c','a',3)
    addEdge(city,'c','x',5)
    addEdge(city,'x','c',5)
    addEdge(city,'x','p',8)
    addEdge(city,'x','l',5)
    addEdge(city,'l','x',5)
    addEdge(city,'l','e',7)
    addEdge(city,'p','x',8)
    addEdge(city,'p','f',1)
    addEdge(city,'p','e',0)
    addEdge(city,'f','p',1)
    addEdge(city,'f','d',3)
    addEdge(city,'f','b',6)
    addEdge(city,'d','f',3)
    addEdge(city,'d','a',0)
    addEdge(city,'d','g',7)
    addEdge(city,'g','d',7)
    addEdge(city,'g','a',1)
    addEdge(city,'g','b',0)
    addEdge(city,'b','g',0)
    addEdge(city,'b','f',6)
    addEdge(city,'b','e',6)
    addEdge(city,'e','p',0)
    addEdge(city,'e','b',6)
    addEdge(city,'e','l',7)
    source_node = 'a'

vertex_set = set()
vertex_list = list(city.keys())

L = len(city)

for i in range(L):
    vertex_set.add(vertex_list[i])

super_vertex_set = defaultdict(list)

for i in range(L+1):
    super_vertex_set[i].append(findsubsets(vertex_set,i))

#Remove all sets that do not have the source node in them
for i in range(2,L+1):
    temp = super_vertex_set[i][0]
    len_temp = len(temp)
    temp2 = []
    for j in range(len(temp)):
        temp1 = temp[j]
        if source_node not in temp1:
            temp2.append(j)  
    temp3 = []
    for j in range(len(temp)):
        if j not in temp2:
            temp3.append(temp[j])
    super_vertex_set[i][0]=temp3

# for i in range(L+1):
#     print('Set of size %d --> ' % i ,end="")
#     print(super_vertex_set[i])

# Super set vertex is a list of a list of a list so addressing must be done as supersetvertex[i][0][j] instead of supersetvertex[i][j], i is length based division of the sets


def minDist(dist,sptSet):
    m = sys.maxsize
    min_index = -1
    for i in range(L):
        if((sptSet[i]==False)&(dist[i]<=m)):
            m = dist[i]
            min_index = i
    return min_index

#Returns a list with distances from src to all other nodes
def dijkstra(src):
    sptSet = []
    dist = []
    for i in range(L):
        dist.append(sys.maxsize)
        sptSet.append(False)
    
    dist[src]=0
    
    for i in range(L):
        u = minDist(dist,sptSet)
        sptSet[u]=True
        for j in range(0,L):
            word = True
            try:
                weights[list(city.keys())[u]][city[list(city.keys())[u]].index(list(city.keys())[j])]
            except:
                word=False
            if(word):
                if((sptSet[j]==False)&(dist[u]!=sys.maxsize)&((dist[u] + weights[list(city.keys())[u]][city[list(city.keys())[u]].index(list(city.keys())[j])])<dist[j])):
                    dist[j] = dist[u] + weights[list(city.keys())[u]][city[list(city.keys())[u]].index(list(city.keys())[j])]
    return dist

distances = np.zeros(shape=(L,L),dtype=int)

for i in range(L):
    dist = dijkstra(i)
    for j in range(L):
        distances[i][j]=dist[j]
        
for i in range(L):
    print("Single source paths from ",end="")
    print(list(city.keys())[i],end=" is --> ")
    print(distances[i])

# Dp implementation of the Algorithm begins here

cost = np.zeros(shape=(L+1,L),dtype=int) #Matrix for Length of paths vs each node

for i in range(L):
    cost[2][i] = distances[0][i]
    
def find_index_j():

for i in range(3,L+1): # Addressing all set sizes
    for j in range(L): # Addressing each node to which the path exists
        min_val = sys.maxsize
        for k in range(L): # Addressing each set in that size range
            temp = c[find_index_j()][find_index_k()] + distances[k][j])
            if(min_val>temp):
                min_val = temp
    cost[i][j] = min_val

print(cost)
