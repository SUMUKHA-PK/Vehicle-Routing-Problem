from collections import defaultdict
import time
import numpy as np
import itertools

start = time.time()

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

    # a----------9---------b
    # |                    |
    # |                    |
    # |                    |
    # 8                    0
    # |                    |
    # |                    |
    # |                    |
    # d----------3---------c

    addEdge(city,'d','a',8) 
    addEdge(city,'a','b',9)
    addEdge(city,'a','d',8) 
    addEdge(city,'b','c',0) 
    addEdge(city,'b','a',9) 
    addEdge(city,'c','d',3) 
    addEdge(city,'c','b',0)  
    addEdge(city,'d','c',3) 
   
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

cost = np.zeros(len(city),dtype=int)


def findsubsets(S,m):
    return frozenset(itertools.combinations(S, m))

vertex_set = set()
vertex_list = list(city.keys())

for i in range(len(city)):
    vertex_set.add(vertex_list[i])

super_vertex_set = set()

for i in range(len(city)):
    super_vertex_set.add( findsubsets(vertex_set,i) )


print(super_vertex_set)