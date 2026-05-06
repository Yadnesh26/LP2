# -------- Kruskal Algorithm -------- #

class UnionFind:
    def __init__(self, vertices):
        # Parent and rank dictionaries
        self.parent = {}
        self.rank = {}

        # Initially every vertex is its own parent
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        # Already in same set
        if px == py:
            return False

        # Union by Rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py

        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px

        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


def kruskal(edges):

    # Collect all vertices
    vertices = set()

    for u, v, w in edges:
        vertices.add(u)
        vertices.add(v)

    # Create Union-Find object
    uf = UnionFind(vertices)

    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    mst = []
    cost = 0

    # Process edges
    for u, v, w in edges:

        # Add edge if it does not form cycle
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

        # Stop if MST is complete
        if len(mst) == len(vertices) - 1:
            break

    return mst, cost


# -------- Input Graph -------- #

edges = [
    ('A', 'B', 10),
    ('A', 'C', 6),
    ('A', 'D', 5),
    ('B', 'D', 15),
    ('C', 'D', 4)
]


# -------- Run Kruskal Algorithm -------- #

mst, cost = kruskal(edges)


# -------- Output -------- #

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total Cost:", cost)
