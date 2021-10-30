rom collections import defaultdict 
from array import array

grap = {
    0: [9],
    1 : [0],
    2 : [],
    3 : [2, 4, 5],
    4 : [],
    5 : [6],
    6 : [7],
    7 : [3, 10],
    8 : [1, 7],
    9 : [8],
    10 : [11],
    11 : [7],
    12 : []
}

n = 0

for item in grap : 
    n = n + 1

visited = []

for i in range(n) :
    visited.append(False)

def dfs(node) : 
    if visited[node] : 
        return  
    visited[node] = True
    print(node)
    neighbours = grap[node]

    for i in neighbours : 
        dfs(i)

start_node = int(input("Input node : "))

dfs(start_node)
