class Anagram: 

    def __init__(self, word):
        self.word = word

    def match(self, match_list): 
        return [test_word for test_word in match_list if (sorted(self.word) == sorted(test_word))]