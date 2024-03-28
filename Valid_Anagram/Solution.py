class Solution:
    def isAnagram(self, s, t) -> bool:
        """
        type s: str
        type t: str
        rtype: bool
        """
        #Run time O(n)
        #Space: O(26) = O(1)
        numberOfLetters = 26

        if len(s) != len(t):
            return False
        
        count = [0] * numberOfLetters

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True
