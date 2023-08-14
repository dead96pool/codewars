"""
link: https://www.codewars.com/kata/5264d2b162488dc400000001/python
"""

def spinWords(sentence):
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


if __name__ == "__main__":
    # testing the output if expected
    print(spinWords( "Hey fellow warriors" ) == "Hey wollef sroirraw")      #=> returns "Hey wollef sroirraw" 
    print(spinWords( "This is a test") == "This is a test")                 #=> returns "This is a test" 
    print(spinWords( "This is another test" ) == "This is rehtona test")    #=> returns "This is rehtona test"