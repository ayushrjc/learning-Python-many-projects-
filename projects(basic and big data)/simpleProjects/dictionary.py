import json
from difflib import get_close_matches


#YOU CAN SEARCH FOR ANY JSON FILE IN GOOGLE LIKE PHYSICS MEANING WORDS
y = json.load(open("original.json"))

def translate(word):
    word = word.lower()
    if word in y:
        return (y[word])
    elif word.title() in y:
        return y[word.title()]
    elif word.upper() in y:
        return y[word.upper()]
    elif len(get_close_matches(word,y.keys())) > 0:
        print("Are you Searching for %s" %get_close_matches((word,y.keys())))
        decide = input("press y for yes or n for no")
        if decide == 'y':
            return y[get_close_matches(word,y.keys())[0]]
        elif decide =="n":
            return("Try again :) ")
        else:
            return ("Meaning not found")
    else:
        print("Meaning not found")

word = input("Enter the word to search meaning\n")
op = translate(word)

if type(op) == list:
    for i in op:
        print(i)
else:
    print(op)


######## use get_close_matches from difflib library ########