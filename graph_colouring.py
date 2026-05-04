def is_safe(node, graph, colors, current_color): 
    # Check if any adjacent vertex has the same color 
    for neighbor in graph.get(node, []): 
        if neighbor in colors and colors[neighbor] == current_color: 
            return False 
    return True 
 
def graph_coloring(graph, m, nodes, index, colors): 
    # Base Case: All nodes are colored 
    if index == len(nodes): 
        return True 
 
    current_node = nodes[index] 
 
    # Try different colors (The "Branching") 
    for color_id in range(1, m + 1): 
        if is_safe(current_node, graph, colors, color_id): 
            # Assign color 
            colors[current_node] = color_id 
 
            # Recur to color the rest of the nodes 
            if graph_coloring(graph, m, nodes, index + 1, colors): 
                return True 
 
            # Backtrack (Remove color) 
            del colors[current_node] 
 
    return False 
 
# --- Built-in Input --- 
# Undirected Graph 
# A -- B 
# | \  | 
# C -- D 
adj_graph = { 
    'A': ['B', 'C', 'D'], 
    'B': ['A', 'D'], 
    'C': ['A', 'D'], 
    'D': ['A', 'B', 'C'] 
} 
 
nodes_list = list(adj_graph.keys()) 
max_colors = 3  # Try to color with 3 colors 
node_colors = {} 
 
# --- Execution --- 
print(f"Attempting to color graph with {max_colors} colors...") 
 
if graph_coloring(adj_graph, max_colors, nodes_list, 0, node_colors): 
    print("Solution Found:") 
    for node, color in node_colors.items(): 
        print(f"Node {node} -> Color {color}") 
else: 
    print("No solution exists with this many colors.")