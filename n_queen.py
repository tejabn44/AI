def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        print_solution(board, n)
        return True  # To print only one solution, return here

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens_backtracking(board, row + 1, n) or res
            board[row][col] = 0  # Backtrack
    return res

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()





def solve_n_queens_branch_and_bound(row, n, cols, diag1, diag2, board):
    if row == n:
        print_solution(board, n)
        return True  # To print only one solution, return here

    res = False
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            board[row][col] = 1
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

            res = solve_n_queens_branch_and_bound(row + 1, n, cols, diag1, diag2, board) or res

            board[row][col] = 0
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
    return res





n = int(input("Enter the number of queens (N): "))
print("\nSolutions using Backtracking:\n")
board = [[0] * n for _ in range(n)]
solve_n_queens_backtracking(board, 0, n)

print("\nSolutions using Branch and Bound:\n")
board = [[0] * n for _ in range(n)]
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
solve_n_queens_branch_and_bound(0, n, cols, diag1, diag2, board)
