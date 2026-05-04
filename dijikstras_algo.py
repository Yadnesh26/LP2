import heapq 
 
def dijkstra(graph, start_node): 
    # distances stores the shortest distance from start_node to every other node 
    # Initialize with infinity 
    distances = {node: float('infinity') for node in graph} 
    distances[start_node] = 0 
     
    # priority_queue stores (distance, current_node) 
    pq = [(0, start_node)] 
     
    # To track the path 
    predecessors = {node: None for node in graph} 
 
    while pq: 
        current_distance, current_node = heapq.heappop(pq) 
 
        # Nodes can be added to the priority queue multiple times.  
        # We only process the shortest distance found so far. 
        if current_distance > distances[current_node]: 
            continue 
 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # Greedy Choice: If a shorter path to neighbor is found 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                predecessors[neighbor] = current_node 
                heapq.heappush(pq, (distance, neighbor)) 
     
    return distances, predecessors 
 
# --- Built-in Input --- 
# Weighted Graph 
graph = { 
    'A': {'B': 5, 'C': 2}, 
    'B': {'D': 4, 'E': 2}, 
    'C': {'B': 8, 'E': 7}, 
    'D': {'E': 6, 'F': 3}, 
    'E': {'F': 1}, 
    'F': {} 
} 
 
start = 'A' 
min_distances, path_tree = dijkstra(graph, start) 
 
# --- Output --- 
print(f"Shortest distances from starting node {start}:") 
print("-" * 40) 
for node, dist in min_distances.items(): 
    print(f"To {node}: {dist}") 