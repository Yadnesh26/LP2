import heapq 
 
def prims_algorithm(graph, start_node): 
    # mst will store the edges of the tree: (weight, from_node, to_node) 
    mst = [] 
    visited = set() 
     
    # edges_heap stores: (cost, from_node, to_node) 
    edges_heap = [] 
     
    # Start by visiting the first node 
    visited.add(start_node) 
     
    # Add all edges from the start node to the heap 
    for neighbor, weight in graph[start_node].items(): 
        heapq.heappush(edges_heap, (weight, start_node, neighbor)) 
     
    total_cost = 0 
     
    while edges_heap: 
        cost, u, v = heapq.heappop(edges_heap) 
         
        # If the destination node is already in the MST, skip it (Greedy check) 
        if v in visited: 
            continue 
         
        # Add edge to MST 
        visited.add(v) 
        mst.append((u, v, cost)) 
        total_cost += cost 
         
        # Add all edges from the new node to the heap 
        for neighbor, weight in graph[v].items(): 
            if neighbor not in visited: 
                heapq.heappush(edges_heap, (weight, v, neighbor)) 
                 
    return mst, total_cost 
 
# --- Built-in Input --- 
# Graph represented as: { 'Node': {'Neighbor': Weight, ...}, ... } 
weighted_graph = { 
    'A': {'B': 2, 'C': 3}, 
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4}, 
    'C': {'A': 3, 'B': 1, 'F': 5}, 
    'D': {'B': 1, 'E': 1}, 
    'E': {'B': 4, 'D': 1, 'F': 1}, 
    'F': {'C': 5, 'E': 1} 
} 
 
start = 'A' 
mst_result, total_weight = prims_algorithm(weighted_graph, start) 
 
# --- Output --- 
print(f"Minimum Spanning Tree starting from {start}:") 
for u, v, weight in mst_result: 
    print(f"Edge: {u} - {v} | Cost: {weight}") 
 
print(f"\nTotal MST Weight: {total_weight}") 