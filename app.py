import json


dictionary = json.load(open("data.json" , 'r'))
def meaning(w):
    return dictionary[w]

word  = input("Enter the word    :     ")
print(meaning(word))
