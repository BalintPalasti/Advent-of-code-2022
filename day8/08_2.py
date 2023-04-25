def fill_grid_from_data():
    grid = []
    grid_rows = []
    grid_columns = []
    row_no = 0
    col_no = 0
    with open('08.txt') as f:
        for line in f:
            grid.append([])
            for char_read in line:
                if char_read == '\n':
                    row_no += 1
                    col_no = 0
                    break
                grid[row_no].append(int(char_read))
                col_no += 1
    

    return grid

def find_visible_trees(grid):
    scenic_score_max = 1
    
    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            scenic_score_act = 1
            ###This section checks all the elements of the grid
            if row_id in (0, len(grid)-1) or col_id in (0, len(grid)-1):            #edges
                continue

            # Check the row of the element (right side):
            counter = 0
            for comp_col_id in range(col_id + 1, len(grid)):
                counter += 1
                if grid[row_id][comp_col_id] >= grid[row_id][col_id] or comp_col_id == len(grid)-1:
                    scenic_score_act *= counter
                    break
            # Check the row of the element (left side):
            counter = 0
            for comp_col_id in range(col_id - 1 - len(grid), -len(grid)-1, -1):
                counter += 1
                if grid[row_id][comp_col_id] >= grid[row_id][col_id] or comp_col_id == - len(grid):
                    scenic_score_act *= counter
                    break

            # Check the column of the element (down side):
            counter = 0
            for comp_row_id in range(row_id + 1, len(grid)):
                counter += 1
                if grid[comp_row_id][col_id] >= grid[row_id][col_id] or comp_row_id == len(grid)-1:
                    scenic_score_act *= counter
                    break

            # Check the column of the element (up side):
            counter = 0
            for comp_row_id in range(row_id - 1 - len(grid), -len(grid)-1, -1):
                counter += 1
                if grid[comp_row_id][col_id] >= grid[row_id][col_id] or comp_row_id == - len(grid):
                    scenic_score_act *= counter
                    break



            if scenic_score_act > scenic_score_max:
                scenic_score_max = scenic_score_act
    
    print("Max:", scenic_score_max)




grid= fill_grid_from_data()
find_visible_trees(grid)