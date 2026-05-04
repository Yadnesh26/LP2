def solve_n_queens(n): 
    # board stores the column index for each row: board[row] = col 
    board = [-1] * n 
    solutions = [] 
    # Lookup arrays to check constraints in O(1) 
    cols = [False] * n 
    diag1 = [False] * (2 * n - 1) # row + col 
    diag2 = [False] * (2 * n - 1) # row - col + (n-1) 
    def backtrack(row): 
        # Base Case: All queens placed 
        if row == n: 
            solutions.append(list(board)) 
            return 
        for col in range(n): 
            # Check Constraints (The "Bound" part) 
            if not (cols[col] or diag1[row + col] or diag2[row - col + n - 1]):         
                # Place Queen 
                board[row] = col 
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True 
                # Move to next row 
                backtrack(row + 1) 
                # Backtrack (Remove Queen) 
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False 
    backtrack(0) 
    return solutions 
def print_board(solution): 
    n = len(solution) 
    for row in solution: 
        line = ["Q" if i == row else "." for i in range(n)] 
        print(" ".join(line)) 
    print("\n") 
# --- Built-in Input --- 
n_size = 5 
results = solve_n_queens(n_size) 
print(f"Found {len(results)} solutions for {n_size}-Queens:\n") 
for sol in results: 
    print_board(sol) 