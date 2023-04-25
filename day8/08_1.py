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
    sum_visible_trees = 0
    for row_id in range(len(grid)):
        for col_id in range(len(grid[row_id])):
            ###This section checks all the elements of the grid
            if row_id in (0, len(grid)-1) or col_id in (0, len(grid)-1):            #edges automaticly counted
                sum_visible_trees +=1
                continue

            found_higher = False

            # Check the row of the element (from left):
            for comp_col_id in range(col_id):
                if grid[row_id][comp_col_id] >= grid[row_id][col_id]:               #kitakarva
                    found_higher = True
                    break
            if not found_higher:
                sum_visible_trees += 1
            # Check the row of the element (from right):
            if found_higher:
                found_higher = False
                for comp_col_id in range(-1, col_id-len(grid), -1):
                    if grid[row_id][comp_col_id] >= grid[row_id][col_id]:               #kitakarva
                        found_higher = True
                        break
                if not found_higher:
                    sum_visible_trees += 1
            # Check the column of the element (from up):
            if found_higher:
                found_higher = False
                for row_col_id in range(row_id):
                    if grid[row_col_id][col_id] >= grid[row_id][col_id]:               #kitakarva
                        found_higher = True
                        break
                if not found_higher:
                    sum_visible_trees += 1
            # Check the column of the element (from down):
            if found_higher:
                found_higher = False
                for comp_row_id in range(-1, row_id-len(grid), -1):
                    if grid[comp_row_id][col_id] >= grid[row_id][col_id]:               #kitakarva
                        found_higher = True
                        break
                if not found_higher:
                    sum_visible_trees += 1

    print('Sum:', sum_visible_trees)

grid= fill_grid_from_data()
find_visible_trees(grid)