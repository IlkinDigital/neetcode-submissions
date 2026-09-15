class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = set()
        max_len = 0
        l = 0
        r = 0
        

        while r < len(s):
            if s[r] not in used:
                used.add(s[r])
                r += 1
                max_len = max(max_len, len(used))
            elif s[r] in used:
                used.remove(s[l])
                l += 1
        
        return max_len

