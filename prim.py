import sys

def prim_mst(graph, V):
    selected = [False] * V
    selected[0] = True  # Start from vertex 0
    edge_count = 0
    mst_cost = 0

    print("Edge : Weight")

    while edge_count < V - 1:
        min_weight = sys.maxsize
        x = 0  # start vertex
        y = 0  # end vertex

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        mst_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    print("Total cost of MST:", mst_cost)

# Take input from user
V = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (0 if no edge):")
graph = []

for i in range(V):
    row = []
    for j in range(V):
        weight = int(input(f"Weight from {i} to {j}: "))
        row.append(weight)
    graph.append(row)

# Run Prim's Algorithm
prim_mst(graph, V)
