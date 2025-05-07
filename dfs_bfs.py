# graph = {}
# num_edges = int(input("Enter number of edges: "))

# print("Enter edges (format: from to):")
# for _ in range(num_edges):
#     u, v = input().split()
#     if u not in graph:
#         graph[u] = []
#     if v not in graph:
#         graph[v] = []
#     graph[u].append(v)
#     graph[v].append(u)  # Add reverse edge for undirected graph

# visited = set()

# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node, end=" ")
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(graph, neighbor, visited)

# start_node = input("Enter start node: ")
# print("DFS traversal:")
# dfs(graph, start_node, visited)








from collections import deque

graph = {}
num_edges = int(input("Enter number of edges: "))

print("Enter edges (format: from to):")
for _ in range(num_edges):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected: add both directions

visited = set()

def bfs(graph, start_node):
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

start_node = input("Enter start node: ")
print("BFS traversal:")
bfs(graph, start_node)
