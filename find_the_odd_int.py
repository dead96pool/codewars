from collections import Counter

def find_it(seq):
    """
    result = [num for num in Counter(seq).keys() if Counter(seq).values()%2 != 0]
    print(result)
    """
    result = 0
    for num in seq:
        result ^= num
    return result 



def assert_equals(output, expected):
    print(output == expected)

if __name__ == "__main__":
    assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
    assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
    assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)