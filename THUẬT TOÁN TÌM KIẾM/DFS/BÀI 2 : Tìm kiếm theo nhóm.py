from collections import defaultdict 
from array import array

grap = {
    #Group 1 :
    6 :  [7, 11],
    7 :  [6, 11],
    11 : [6, 7],
    #Group 2 :
    4 :  [0, 8],
    0 :  [4, 8, 14, 13],
    14 : [8, 0, 13],
    8 : [0, 4, 14],
    13 : [0, 14], 
    #Group 3 : 
    3 : [9], 
    9 : [2, 3, 15], 
    2 : [9, 15],
    15 : [2, 9, 10],
    10 : [15],
    #Group 4 :
    1 : [5], 
    5 : [1, 16, 17],
    16 : [5], 
    17 : [5],
    #Group 5 : 
    12 : []
}


def dfs (node, count, visited) : 
    visited[node] = True
    print(node)
    components.append(count)
    for item in grap[node] : 
        if visited[item] == False : 
            dfs(item, count, visited)
    return


def findComponents(n, count, visited) : 
    for node in range(n) :
        if visited[node] == False : 
            print("Group" , count ,":")
            dfs(node, count, visited)
            count = count + 1
    return 



count = 1
n = 0
for item in grap :
    n = n + 1; 
visited = []
components = []
for item in range(n) : 
    visited.append(False)

findComponents(n, count, visited)

