# Sudoku Solver

def sudoku(puzzle):
    def solve(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for k in range(1, 10):
                        if check(puzzle, i, j, k):
                            puzzle[i][j] = k
                            if solve(puzzle):
                                return puzzle
                            puzzle[i][j] = 0
                    return False
        return puzzle

    def check(puzzle, i, j, k):
        for l in range(9):
            if puzzle[i][l] == k or puzzle[l][j] == k:
                return False
        for l in range(3):
            for m in range(3):
                if puzzle[(i // 3) * 3 + l][(j // 3) * 3 + m] == k:
                    return False
        return True

    return solve(puzzle)