from itertools import permutations


def anagrams(word, dictionary):
    return [
        "".join(i)
        for i in permutations(list(word), len(word))
        if "".join(i) in dictionary
    ]
