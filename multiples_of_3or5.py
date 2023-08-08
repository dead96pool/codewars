"""
link: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""


def solution(number):
    num_list = [num for num in range(number) if num%5 == 0 or num%3 == 0]
    """for char in range(number):
        if char%5 == 0 or char%3 == 0:
            sum.append(char)
"""
    return sum(num_list)

def assert_equals(output, expected):
    print(output == expected)
    

if __name__ == "__main__":
    assert_equals(solution(4), 3)
    assert_equals(solution(6), 8)
    assert_equals(solution(16), 60)
    assert_equals(solution(3), 0)
    assert_equals(solution(5), 3)
    assert_equals(solution(-1), 0)
    assert_equals(solution(200), 9168)