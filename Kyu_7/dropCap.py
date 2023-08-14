import re


def drop_cap(words):
    words = words.lower()
    print(words)

    blacklist = ["the", "of", "in"]
    
    word_list = re.split('([^a-zA-Z0-9+]+)', words)
    print(word_list)
    
    
    words = "".join([word.capitalize() if word not in blacklist else word for word in word_list])
    print(words)


    return words





drop_cap('apple')               #'Apple'
drop_cap('apple of banana')     #'Apple of Banana'
drop_cap('one   space')         #'One   Space'
drop_cap('   space WALK   ')    #'   Space Walk   '
drop_cap('')                    #''