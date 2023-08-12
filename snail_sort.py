"""
link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
"""

def snail(array):
    snail_sort = []
    
    while array:
        # right
        snail_sort.extend(array.pop(0))

        # down
        for row in array:
            snail_sort.append(row.pop())

        # left
        if array:
            snail_sort.extend(array.pop()[::-1])

        # up
        for row in array[::-1]:
            snail_sort.append(row.pop(0))

    return snail_sort


def result_check(output, expected):
    print(output == expected)

if __name__ == "__main__":
    
    array = [[1, 2, 3, 1],
             [4, 5, 6, 4],
             [7, 8, 9, 7],
             [12, 11, 10, 14]]
    
    result_check(snail(array), [1,2,3,1,4,7,14,10,11,12,7,4,5,6,9,8]) #=> [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8] """

    array = [[1, 2, 3, 4, 5, 6],
             [7, 8, 9, 10, 11, 12],
             [13, 14, 15, 16, 17, 18],
             [19, 20, 21, 22, 23, 24],
             [25, 26, 27, 28, 29, 30],
             [31, 32, 33, 34, 35, 36]]

    result_check(snail(array), 
                 [1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 35, 34, 33, 32, 31, 25, 19, 13, 7, 8, 9, 10, 11, 17, 23, 29, 28, 27, 26, 20, 14, 15, 16, 22, 21])

    
    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    
    result_check(snail(array), [1,2,3,4,5,6,7,8,9]) #=> [1,2,3,4,5,6,7,8,9]
    