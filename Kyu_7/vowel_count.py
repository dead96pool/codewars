"""
link: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""
import re

def get_count(sentence):
#    return len(re.findall(r"[aeiou]", sentence))

    print(sum(c in "aeiou" for c in sentence))

    return None


def main():
    count = get_count("abracadabra")
    print(count)

if __name__ == "__main__":
    main()