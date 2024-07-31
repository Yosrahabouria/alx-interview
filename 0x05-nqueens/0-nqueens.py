#!/usr/bin/python3
"""
Solution to the N queens problem
"""
import sys


def solve_nqueens(row, size, columns, pos_diags, neg_diags, board):
    if row == size:
        solution = []
        for r in range(size):
            for c in range(size):
                if board[r][c] == 1:
                    solution.append([r, c])
        print(solution)
        return

    for col in range(size):
        if col in columns or (row + col) in pos_diags or (row - col) in neg_diags:
            continue

        columns.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        board[row][col] = 1

        solve_nqueens(row + 1, size, columns, pos_diags, neg_diags, board)

        columns.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        board[row][col] = 0


def nqueens(size):
    columns = set()
    pos_diags = set()
    neg_diags = set()
    board = [[0] * size for _ in range(size)]

    solve_nqueens(0, size, columns, pos_diags, neg_diags, board)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(size)
