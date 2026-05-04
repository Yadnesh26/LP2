from collections import deque 
 
# --- Algorithm Definitions --- 
 
def dfs_recursive(graph, vertex, visited=None): 
    if visited is None: 
        visited = set() 
     
    # Mark and Print 
    visited.add(vertex) 
    print(vertex, end=" ") 
 
    # Visit neighbors deep first 
    for neighbor in graph.get(vertex, []): 
        if neighbor not in visited: 
            dfs_recursive(graph, neighbor, visited) 
 
#Breadth First Search 
 
def bfs_recursive(graph, queue, visited): 
    if not queue: 
        return 
     
    # Process current level node 
    vertex = queue.popleft() 
    print(vertex, end=" ") 
 
    # Add all unvisited neighbors to the queue for the next recursive steps 
    for neighbor in graph.get(vertex, []): 
        if neighbor not in visited: 
            visited.add(neighbor) 
            queue.append(neighbor) 
             
    # Tail recursion to process the next item in the queue 
    bfs_recursive(graph, queue, visited) 
 
# --- Built-in Data Setup --- 
 
# This represents an undirected graph: 
# A -- B -- D 
# |    | 
# C ---- 
built_in_graph = { 
'A': ['B', 'C'], 
'B': ['A', 'C', 'D'], 
'C': ['A', 'B'], 
'D': ['B'] 
} 
start_node = 'A' 
# --- Execution --- 
print(f"Starting traversal from vertex: {start_node}") 
print("-" * 30) 
print("DFS Recursive Path:") 
dfs_recursive(built_in_graph, start_node) 
print("\n\nBFS Recursive Path:") 
# BFS requires the queue and visited set to be initialized with the start node 
q = deque([start_node]) 
v = {start_node} 
bfs_recursive(built_in_graph, q, v) 
print()