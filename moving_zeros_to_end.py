"""
link: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""
import time

def move_zeros(lst):
    
    lst.count(0)
    mod_lst = [num for num in lst if num != 0]
    #mod_lst.extend(lst.count(0)*[0])
    

    """for idx, num in enumerate(lst):
        if num == 0:
            lst.remove(lst[idx])
            lst.extend([0])"""
    return mod_lst + [0] * lst.count(0)

    

def assert_equals(arr, correct):
    print(arr == correct)

if __name__ == "__main__":
    start_time = time.time()
    assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    
    assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    assert_equals(move_zeros([0, 0]), [0, 0])
    assert_equals(move_zeros([0]), [0])
    assert_equals(move_zeros([]), [])

    print("Process finished --- %s seconds ---" % (time.time() - start_time))