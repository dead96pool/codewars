"""
link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
"""

def duplicate_encode(word):
    new_str = ""
    word = word.lower()

    new_str = "".join(["(" if word.count(char) == 1 else ")" for char in word])
    
    return new_str
"""
    for char in word:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1 

    for char in word:
        if seen[char] == 1:
            new_str += "("
        else:
            new_str += ")"

    return new_str
"""
def main():
    result = duplicate_encode("Success")
    print(result)


if __name__ == "__main__":
    main()