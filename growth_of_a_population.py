"""
link: https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python
"""

def nb_year(p0, percent, aug, p, years = 0):
    
    if p0 < p:
        return nb_year(p0 + int(p0 * percent/100) + aug, percent, aug, p, years + 1)
    return years
""" while cur_p < p:
    cur_p += int(cur_p * (percent/100) + aug)
    time += 1"""        
    


if __name__ == "__main__":
    print(nb_year(1500, 5, 100, 5000))
    print(nb_year(1500000, 2.5, 10000, 2000000))
    print(nb_year(1500000, 0.25, 1000, 2000000))