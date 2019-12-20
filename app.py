import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

def meaning(w):
    if w in dictionary:
        return dictionary[w]
    elif w.title() in dictionary:
        return dictionary[w.title()]
    elif len(get_close_matches(w,dictionary.keys()))>0:
        yn = input("Did You mean %s instead ? Please enter Y for yes and N for no....  " % get_close_matches(w,dictionary.keys())[0])
        if yn=="Y":
            return dictionary[get_close_matches(w,dictionary.keys())[0]]
        elif yn == "N":
            return "we don't understand your language .Are you an alien?"
        else:
            return "we don't understand your language .Are you an alien? "
    else:
        return "we don't understand your language .Are you an alien?"

word  = input("Enter the word    :     ")
output = (meaning(word.lower()))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
