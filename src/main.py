import sys
from words import anagrams

if __name__ == "__main__":
    with open("src/words.txt", "r", encoding="utf8") as stream:
        all_words = stream.read().split("\n")

    if len(sys.argv) <= 1:
        print("Give me something to anagram!")
    else:
        print(anagrams(sys.argv[1], all_words))
