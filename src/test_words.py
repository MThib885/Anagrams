from words import anagrams


def test_anagrams():
    assert anagrams("", []) == []
    assert anagrams("a", ["a"]) == ["a"]

    assert anagrams("abc", []) == []
    assert anagrams("", ["cab"]) == []

    assert anagrams("abc", ["bac", "cab", "def"]) == ["bac", "cab"]
