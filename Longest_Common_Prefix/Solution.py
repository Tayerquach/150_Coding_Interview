class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        type strs: List[str]
        rtype: str
        """
        if len(strs) == 0:
            return ""
        
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]: #From the second word
                if i == len(word) or word[i] != base[i]:
                    return base[:i]
        return base