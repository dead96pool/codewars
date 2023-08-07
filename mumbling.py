"""
link: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/python
"""


def accum(s):
    return "-".join(char.upper()+idx*char for idx,char in enumerate(s.lower()))
    

if __name__ == "__main__":
    print(accum("abcd")) #-> "A-Bb-Ccc-Dddd"
    print(accum("ZpglnRxqenU"))#, "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
    print(accum("NyffsGeyylB"))#, "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
    print(accum("MjtkuBovqrU"))#, "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
    print(accum("EvidjUnokmM"))#, "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
    print(accum("HbideVbxncC"))