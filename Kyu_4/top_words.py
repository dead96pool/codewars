from collections import Counter
import re

def top_words(text):
    words = re.findall(r"[A-Za-z']+", text.lower())
    word_counts = Counter(words)

    filtered_word_counts = {word: count for word, count in word_counts.items() if word != "'" * len(word)}
        
    top_words = sorted(filtered_word_counts, key=lambda word: (-word_counts[word], word))
    
    print(top_words[:3])

if __name__ == "__main__":
    
    string = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""
    top_words(string)     # => ["a", "of", "on"]
    
    top_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
    # => ["e", "ddd", "aa"]
    
    top_words("  //wont won't won't")
    # => ["won't", "wont"]

    top_words("''''")

    top_words(" ''', 'I', 'am', 'here', ''' ")