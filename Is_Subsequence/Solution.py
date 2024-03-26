class Solution:
    def isSubsequence(self, s, t) -> bool:
        """
        type s: str
        type t: str
        rtype: bool
        """
        i = 0 # pointer for s
        j = 0 # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        return i == len(s)
