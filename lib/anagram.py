# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams = []
        ana_word = sorted(self.word)

        for word in list:
            if len(word) == len(self.word) and word.lower() != self.word:
                list_letters = sorted(word.lower())
                if ana_word == list_letters:
                    anagrams.append(word)

        return anagrams
