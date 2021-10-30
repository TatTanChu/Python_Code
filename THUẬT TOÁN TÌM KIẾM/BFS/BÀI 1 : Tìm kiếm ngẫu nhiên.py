grap = {
    0 : [9, 7, 11], 
    1 : [8, 10],
    2 : [3, 12],
    3 : [7, 2, 4],
    4 : [3],
    5 : [6],
    6 : [5, 7],
    7 : [11, 6, 3], 
    8 : [1, 12, 9], 
    9 : [10, 8, 0], 
    10 : [1, 9], 
    11 : [0, 7],
    12 : [2, 8]
}

n = 0

for node in grap : 
    n = n + 1; 

visited = []

for i in range(n) : 
    visited.append(False)

def BFS (start_Node) : 
    q = []
    visited[start_Node] = True
    q.append(start_Node) 
    
    while len(q) != 0 : 
        Node = q.pop(0)
        print(Node)
        neighbours = grap[Node]

        for i in neighbours : 
            if visited[i] == False : 
                visited[i] = True 
                q.append(i)

BFS(0)

    
        
