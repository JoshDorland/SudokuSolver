#The unsolved sudoku board.
board = [
    [0,0,0,0,0,0,2,0,0],
    [0,8,0,0,0,7,0,9,0],
    [6,0,2,0,0,0,5,0,0],
    [0,7,0,0,6,0,0,0,0],
    [0,0,0,9,0,1,0,0,0],
    [0,0,0,0,2,0,0,4,0],
    [0,0,5,0,0,0,6,0,3],
    [0,9,0,4,0,0,0,7,0],
    [0,0,6,0,0,0,0,0,0]
]

#Prints the sudoku board
def printBoard(bo):

    #Rows
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        #Columns
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "") #By default the print statement will print a new line so the , end = "" will keep it on the same line
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = "")

#Checks if the current spot is empty (contains a 0) and returns the position
def findEmpty(bo):

    #Rows 
    for i in range(len(bo)):
        #Columns
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

#This function will check if the value from 1 - 9 is valid and follows the rules of Sudoku
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            #Recursion means being able to call a function within itself. It will go through again with the new board after adding i to 
            # bo[row][col] if this is works it will keep going if not it will set the value to 0 and go back to the original and try a
            # new value.

            if solve(bo): 
                return True

            bo[row][col] = 0

    return False

print("Initial Board.")
printBoard(board)
print("_________________________")
print("Solved Board.")
solve(board)
printBoard(board)