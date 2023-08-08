"""
link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python
"""
import time
start_time = time.time()

def high(str):
    """max_score, max_idx = 0, 0
    str_list = str.split()

    for idx, word in enumerate(str_list):
        word_score = 0
        for char in word:
            word_score += ord(char) - 96
        
        if word_score > max_score:
            max_idx = idx
            max_score = word_score
        
    return str_list[max_idx]
"""
    return max(str.split(), key=lambda k: sum(ord(c) - 96 for c in k))
string = "what time are we climbing up to the volcano"
print(high(string))


print("Process finished --- %.100f seconds ---" % (time.time() - start_time))