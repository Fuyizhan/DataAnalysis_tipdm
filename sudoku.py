

def find_empty(puzzle):
    # find row and col ob the puzzle that's not filled yet(rep -1)
    # then return row, col tuple or (None, None) if there is no empty
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # figure out whether the guess at the row/col of the puzzle is a valid guess
    # return true if it's valid, false otherwise

    # start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    # col
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # and then the square(3*3)
    # we should know this value belong to which square
    # (row // 3) * 3  (col // 3) * 3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True





def solve_soduku(puzzle):
    #step 1:choose somewhere on the puzzle to make a guess
    row, col = find_empty(puzzle)
    #step 1.1 : if there's nowhere left, then we win
    if row is None:
        return True
    #step 2: make a guess(1-9) and put it into puzzle
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_soduku(puzzle):
                return True
        puzzle[row][col] = -1

    # unsolvable
    return False

