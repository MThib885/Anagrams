from itertools import permutations

def anagrams(word):
    return ["".join(i) for i in permutations(list(word),len(word))]    

print(anagrams("abc"))
