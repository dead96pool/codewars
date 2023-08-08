"""
link: https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""

def pig_it(str):
    str_lst = str.split()

    """
    for idx, word in enumerate(str_lst):
        if word.isalpha():
            str_lst[idx] = word[1:] + word[0] + "ay"
    """
    pig_lst = [word[1:] + word[0] + "ay" if word.isalpha() else word for word in str_lst]
    print(" ".join(pig_lst))



if __name__ == "__main__":
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !