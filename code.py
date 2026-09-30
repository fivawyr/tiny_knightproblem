# project idea: recreate knight problem and later visualize it with vpython 

grid =        [[0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
                                ] 

def knight(rows: int , columns: int):
    moveset = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, -1], [-2, 1], [1, -2], [-1, -2]]
    valid_moves = [] 
    for dir_row, dir_columns in moveset: 
        new_row = rows + dir_row
        new_column = columns + dir_columns

        if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]): 
            valid_moves.append((new_row, new_column)) # bound check

    return valid_moves

def draw_grid(): 
    for i in grid: 
        print("\t".join(map(str, i)))
    return 0     


i_row = int(input("Enter your desiered [x] knight position and see all possible moves: \n"))
i_column = int(input("Enter your desiered [y] knight position and see all possible moves: \n"))

grid[i_row][i_column] = 'X'

valid_moves = knight(i_row, i_column)
for row, column in valid_moves:
    grid[row][column] = 'x'

draw_grid()

print(f" The valid moves are: {valid_moves}")
