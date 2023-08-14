

def square_digits(num):
    sq = ""
    
    for digits in str(num):
        sq += str(int(digits)**2)

    return int(sq)




square_digits(9119)     # 811181
square_digits(0)        # 0 