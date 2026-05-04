import heapq 
 
class Node: 
    def __init__(self, position, parent=None): 
        self.position = position 
        self.parent = parent 
        self.g = 0  # Distance from start 
        self.h = 0  # Distance to goal 
        self.f = 0  # Total cost 
 
    def __lt__(self, other): 
        return self.f < other.f 
 
def heuristic(current, goal): 
    # Manhattan distance (for grid movement: up, down, left, right) 
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1]) 
 
def a_star(grid, start, end): 
    start_node = Node(start) 
    end_node = Node(end) 
 
    # open_list stores nodes to be explored (Priority Queue) 
    open_list = [] 
    # closed_list stores nodes already explored 
    closed_list = set() 
 
    heapq.heappush(open_list, start_node) 
 
    while open_list: 
        # Get the node with the lowest f score 
        current_node = heapq.heappop(open_list) 
        closed_list.add(current_node.position) 
 
        # Found the goal! 
        if current_node.position == end_node.position: 
            path = [] 
            while current_node: 
                path.append(current_node.position) 
                current_node = current_node.parent 
            return path[::-1] # Return reversed path 
 
        # Generate neighbors (Up, Down, Left, Right) 
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
        for new_pos in neighbors: 
            node_pos = (current_node.position[0] + new_pos[0],  
                        current_node.position[1] + new_pos[1]) 
            # Check boundaries 
            if (node_pos[0] < 0 or node_pos[0] >= len(grid) or  
                node_pos[1] < 0 or node_pos[1] >= len(grid[0])): 
                continue 
 
            # Check if walkable 
            if grid[node_pos[0]][node_pos[1]] != 0: 
                continue 
 
            # Check if already visited 
            if node_pos in closed_list: 
                continue 
 
            neighbor_node = Node(node_pos, current_node) 
            neighbor_node.g = current_node.g + 1 
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position) 
            neighbor_node.f = neighbor_node.g + neighbor_node.h 
 
            # If neighbor is already in open_list with a lower g, skip it 
            if any(open_node.position == neighbor_node.position and  
                   neighbor_node.g > open_node.g for open_node in open_list): 
                continue 
 
            heapq.heappush(open_list, neighbor_node) 
    return None # No path found 
# --- Built-in Input --- 
grid = [ 
    [0, 0, 0, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0] 
] 
start = (0, 0) 
end = (4, 4) 
path = a_star(grid, start, end) 
 
print(f"Start: {start} | End: {end}") 
print("Path found:", path if path else "No path available") 