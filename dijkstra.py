import sys

def dijkstra(graph, V, start):
    visited = [False] * V
    distance = [sys.maxsize] * V
    distance[start] = 0

    for _ in range(V):
        # Find the unvisited vertex with the smallest distance
        min_dist = sys.maxsize
        u = -1
        for i in range(V):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        if u == -1:
            break  # All remaining vertices are inaccessible

        visited[u] = True

        # Update the distance of neighbors
        for v in range(V):
            if graph[u][v] != 0 and not visited[v]:
                if distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    # Print the results
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t{distance[i]}")



V = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (0 if no edge):")
graph = []

for i in range(V):
    row = []
    for j in range(V):
        w = int(input(f"Weight from {i} to {j}: "))
        row.append(w)
    graph.append(row)

start = int(input("Enter the source vertex: "))
dijkstra(graph, V, start)
