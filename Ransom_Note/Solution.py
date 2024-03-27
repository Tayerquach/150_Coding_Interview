class Solution:
    def canConstruct(self, ransomNote, magazine) -> bool:
        """
        type ransomNote: str
        type magazine: str
        rtype: bool
        """
        # Create a hashmap to store the characters and their frequences
        m_dict = {}
        for char in magazine:
            if char not in m_dict:
                m_dict[char] = 1
            else:
                m_dict[char] += 1

        # Check 
        for c in ransomNote:
            if c not in m_dict or m_dict[c] == 0:
                return False
            else:
                m_dict[c] -= 1
        return True        


