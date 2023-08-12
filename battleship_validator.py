import numpy as np

def validate_battlefield(field):
    # write your magic here
    """
    ship count: 
                1 x 4 cell ship
                2 x 3 cell ship
                3 x 2 cell ship
                4 x 1 cell ship
    
    """
    cell_4 = 1
    cell_3 = 2
    cell_2 = 3
    cell_1 = 4

    print(np.array(field))

    # verify ship count

    # verify ship shape

    # verify ship position
    
    return True



def assert_equals(output, expected):
    print(output == expected)

if __name__ == "__main__":
    battleField = [ [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
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