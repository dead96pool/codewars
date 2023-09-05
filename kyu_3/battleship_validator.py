"""
link: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/python
"""

def validate_battlefield(field):
    ships = {1: 0,      # 4
             2: 0,      # 3
             3: 0,      # 2
             4: 0}      # 1
             
    occupied = set()
    
    def touching(row, col):
        # for the sides
        if row == 0 and 0<col<9:
            return field[row+1][col+1] or field[row+1][col-1]
        elif row == 9 and 0<col<9:
            return field[row-1][col-1] or field[row-1][col+1]
        elif col == 0 and 0<row<9:
            return field[row-1][col+1] or field[row+1][col+1]
        elif col == 9 and 0<row<9:
            return field[row+1][col-1] or field[row-1][col-1]
        # for the corners
        elif row == 0 and col == 0:
            return field[row+1][col+1]
        elif row == 0 and col == 9:
            return field[row+1][col-1]
        elif row == 9 and col == 0:
            return field[row-1][col+1]
        elif row == 9 and col == 9:
            return field[row-1][col-1]
        # for the rest of the grid
        else:
            return field[row+1][col+1] == 1 or field[row-1][col-1] == 1 or field[row+1][col-1] == 1 or field[row-1][col+1] == 1

    # check if not already counted
    def valid_cell(row, col):
        return not touching(row,col) and (row, col) not in occupied
    
    
    
    for row in range(10):
        for col in range(10):
            if field[row][col] == 1:
                # horizontal ships
                if col < 9 and field[row][col+1] == 1 and valid_cell(row,col):
                    size = 1
                    while col + size < 10 and valid_cell(row,col+size) and field[row][col+size] == 1:
                        occupied.add((row,col+size))
                        size += 1
                    if size > 4:
                        return False
                    ships[size] += 1
                # vertical ships
                elif row < 9 and field[row+1][col] == 1 and valid_cell(row,col):
                    size = 1
                    while row + size < 10 and valid_cell(row+size,col) and field[row+size][col] == 1:
                        occupied.add((row+size,col))
                        size += 1
                    if size > 4:
                        return False
                    ships[size] += 1
                # submerines
                elif ((row == 9 or field[row+1][col] == 0) and (col == 9 or field[row][col+1] == 0) and 
                      (row == 0 or field[row-1][col] == 0) and (col == 0 or field[row][col-1] == 0)):
                    size = 1
                    occupied.add((row,col))
                    ships[size] += 1

    print(ships)
    
    return ships == {4:1, 3:2, 2:3, 1:4}

def assert_equals(output, expected):
    print(output == expected)

if __name__ == "__main__":
    battleField = [ [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 0, 1, 1, 1, 0, 0, 0]]   
    
    assert_equals(validate_battlefield(battleField), True)

"""
    battlefield = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 1], 
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
                   [1, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [1, 1, 0, 0, 0, 0, 1, 1, 0, 0], 
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]]"""