"""
link: https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
"""

def bouncing_ball(h, bounce, window):
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    else:
        count = 0
        while window < h:
            count += 1
            h = h*bounce
            if h > window:
                count += 1 
        return count
    

print(bouncing_ball(30, 0.75, 1.5) == 21)
print(bouncing_ball(3, 0.66, 1.5) == 3)