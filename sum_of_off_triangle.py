"""
link: https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
"""

def row_sum_odd_numbers(row):
    # row starting number
    start_num = row*(row-1)+1       
    # row 4: 13 15 17 19
    # row 5: 21 23 25 27 29
    # row 6: 31 33 35 37 39 41
    # row 7: 43 45 47 49 51 53 55
    # row 8: 57 59 ...
    odd = [start_num + 2 * i for i in range(row) ]
    return sum(odd)
    """
    tri = []
    start_num = row*(row-1)-1
    
    for _ in range(row):
        tri.append(start_num+2)
        start_num += 2

    return sum(tri)"""

# check if the result is correct
def assert_equals(number, result):
    print(number == result)

# main
if __name__ == "__main__":
    # checking the result is the expected answer
    assert_equals(row_sum_odd_numbers(1), 1)
    assert_equals(row_sum_odd_numbers(2), 8)
    assert_equals(row_sum_odd_numbers(13), 2197)
    assert_equals(row_sum_odd_numbers(19), 6859)
    assert_equals(row_sum_odd_numbers(41), 68921)