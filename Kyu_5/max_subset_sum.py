

def max_sequence(array):
    if not array:
        return 0
    
    if all([val < 0 for val in array]):
        return 0
    
    max_ending_here = max_so_far = array[0]
    
    for num in array[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))

