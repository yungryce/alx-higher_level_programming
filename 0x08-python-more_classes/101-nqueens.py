#!/usr/bin/python3
import sys
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position.

    Parameters:
    - board: List representing the column positions of queens in each row.
    - row: Row index to check.
    - col: Column index to check.

    Returns:
    - True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row):
    """
    Recursive utility function to solve the N-Queens problem.

    Parameters:
    - board: List representing the column positions of queens in each row.
    - row: Current row being considered.

    Returns:
    - List of solutions, where each solution is a list of positions (row, col).
    """
    if row == len(board):
        return [list(enumerate(board))]

    solutions = []
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solutions.extend(solve_nqueens_util(board, row + 1))
    return solutions


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Parameters:
    - n: Size of the chessboard.

    Returns:
    - List of solutions, where each solution is a list of positions (row, col).
    """
    # board = [[0] * n for _ in range(n)]
    board = [-1] * n
    solutions = solve_nqueens_util(board, 0)
    return solutions


def print_solutions(solutions):
    """
    Print the N-Queens solutions.

    Parameters:
    - solutions: List of solutions, where each solution is a list of
    positions (row, col).
    """
    for solution in solutions:
        print([list(pos) for pos in solution])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print(f"N must be a number")
        sys.exit(1)

    if n >= 4:
        solutions = solve_nqueens(n)
        print_solutions(solutions)
    else:
        print("N must be at least 4")
