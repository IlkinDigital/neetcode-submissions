class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for c in t:
            if c not in freq or freq[c] <= 0:
                return False
            else:
                freq[c] -= 1
        
        for c, n in freq.items():
            if n != 0:
                return False
        
        return True
