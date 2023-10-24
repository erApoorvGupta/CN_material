import sys

def miniDist(distance, visited):
    minimum = sys.maxsize
    ind = 0
    for k in range(len(distance)):
        if not visited[k] and distance[k] <= minimum:
            minimum = distance[k]
            ind = k
    return ind

def DijkstraAlgo(graph):
    num_vertices = len(graph)
    distance = [sys.maxsize] * num_vertices
    visited = [0] * num_vertices
    path = [-1] * num_vertices  # To track the path

    src = int(input("Enter the source vertex: ")) - 1
    dest = int(input("Enter the destination vertex: ")) - 1

    for k in range(num_vertices):   
        distance[k] = sys.maxsize
        visited[k] = 0

    distance[src] = 0

    for i in range(num_vertices):
        m = miniDist(distance, visited)
        visited[m] = 1

        for k in range(num_vertices):
            if not (visited[k] and graph[m][k] and distance[m] != sys.maxsize and 
            distance[m] + graph[m][k] < distance[k]):
                distance[k] = distance[m] + graph[m][k]
                path[k] = m  # Update the path

    # Print the shortest distance
    if distance[dest] == sys.maxsize:
        print(f"No path from {src + 1} to {dest + 1}")
    else:
        print(f"Shortest distance between {src + 1} and {dest + 1} is {distance[dest]}")

        # Print the path
        print("Shortest Path:", end=" ")
        printPath(path, dest)

def printPath(path, dest):
    stack = []
    while path[dest] != -1:
        stack.append(dest + 1)
        dest = path[dest]
    stack.append(dest + 1)
    
    while stack:
        print(stack.pop(), end=" ")

if __name__ == "__main__":
    graph = [
        [0, 2, 0, 0, 0, 0, 6, 0],
        [2, 0, 7, 0, 1, 0, 0, 0],
        [0, 7, 0, 3, 0, 3, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 3, 0, 1, 0, 0, 2],
        [6, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 2, 4, 0]
    ]

    DijkstraAlgo(graph)
