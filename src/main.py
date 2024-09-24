import sys
from itertools import permutations


def anagrams(word):
    return ["".join(i) for i in permutations(list(word),len(word)) if "".join(i) in all_words]    


if __name__ == "__main__":
    with open("src/words.txt","r") as stream:
        all_words = stream.read().split("\n")

    if len(sys.argv) <= 1:
        print("Give me something to anagram!")
    else:
        print(anagrams(sys.argv[1]))
