from itertools import permutations

with open("src/words.txt","r") as stream:
    all_words = stream.read().split("\n")

def anagrams(word):
    return ["".join(i) for i in permutations(list(word),len(word))]    
