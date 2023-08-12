

def validate_battlefield(field):
    # write your magic here
    """
    ship count: 
                1 x 4 cell ship
                2 x 3 cell ship
                3 x 2 cell ship
                4 x 1 cell ship
    
    """




    
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