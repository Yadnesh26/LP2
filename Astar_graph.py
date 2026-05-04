def aStarAlgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()

    g = {}  # cost from start node
    parents = {}  # to store path

    g[start_node] = 0
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # Find node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If no node found
        if n is None:
            print("Path does not exist!")
            return None

        # If goal is reached
        if n == stop_node:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()

            print("Path found:", path)
            return path

        # Explore neighbors
        for (m, weight) in get_neighbors(n):

            # If new node
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                # If better path found
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        # Move n from open to closed
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None


# Graph definition
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return []


# Heuristic values
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return H_dist[n]


# Graph structure
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 2), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)],
    'G': []
}


# Run the algorithm
aStarAlgo('A', 'G')