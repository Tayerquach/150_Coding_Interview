class Solution:
    def wordPattern (self, pattern, s) -> bool:
        """
        type pattern: str
        type s: str
        rtype: bool
        """

        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            elif w in wordToChar and wordToChar[w] != c:
                return False
            
            charToWord[c] = w
            wordToChar[w] = c
        return True