
### if a hashtag is already there in the text then the code adds another one
### so the output for generate_hashtag('# test word') gives ##TestWord

### solution!
# used regex to find only words without punctuations

import re

def generate_hashtag(s):
    #words = s.title().split()
    words = re.findall(r"[A-Za-z]+",s.title())
    hashtag = "#" + "".join(words)

    return False if len(hashtag) > 140 or len(hashtag) == 1 else hashtag


def assert_equals(result, expected,str):
    print(result == expected)

if __name__ == "__main__":
    
    assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
    assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
    assert_equals(generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
    assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
    assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
    assert_equals(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
    assert_equals(generate_hashtag('c i n'), '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
    assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        
    assert_equals(generate_hashtag(''), False, "")
    assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, "")

    assert_equals(generate_hashtag('# test word'), "#TestWord", "")