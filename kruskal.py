class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False

def kruskal_mst(V, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(V)
    mst_cost = 0
    mst_edges = []

    print("Edges in MST:")
    for u, v, w in edges:
        if ds.union(u, v):
            print(f"{u} - {v} : {w}")
            mst_cost += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == V - 1:
                break

    print("Total cost of MST:", mst_cost)

# Take input
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter edges in format: u v weight")
for i in range(E):
    u = int(input(f"Edge {i+1} - From: "))
    v = int(input(f"Edge {i+1} - To: "))
    w = int(input(f"Edge {i+1} - Weight: "))
    edges.append((u, v, w))

# Run Kruskal's Algorithm
kruskal_mst(V, edges)
