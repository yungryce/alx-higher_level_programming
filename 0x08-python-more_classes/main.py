def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = solve_nqueens_util(board, 0)
    return solutions

solve_nqueens(4)
