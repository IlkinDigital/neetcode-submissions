class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        og_freq = [0] * 26
        freq = [0] * 26

        for i in range(len(s1)):
            freq[ord(s2[i]) - ord('a')] += 1

        for c in s1:
            og_freq[ord(c) - ord('a')] += 1

        print(freq)
        print(og_freq)
        
        for i in range(0, len(s2) - len(s1) + 1):
            if og_freq == freq:
                return True
            if i + len(s1) < len(s2):
                freq[ord(s2[i]) - ord('a')] -= 1
                freq[ord(s2[i + len(s1)]) - ord('a')] += 1
        
        return False