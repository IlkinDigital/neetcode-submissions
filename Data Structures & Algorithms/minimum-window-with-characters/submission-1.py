class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
            
        count = {}

        for c in t:
            count[c] = count.get(c, 0) + 1

        need = len(count)
        l = 0
        r = 0
        
        res = (-1, -1)
        curr_count = {}
        have = 0

        while r < len(s):
            curr_count[s[r]] = curr_count.get(s[r], 0) + 1

            if curr_count[s[r]] == count.get(s[r], -1):
                have += 1
            
            while have == need:
                if res == (-1, -1) or res[1] - res[0] > r - l + 1:
                    res = (l, r + 1)

                curr_count[s[l]] -= 1
                if s[l] in count and curr_count[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

            r += 1

        return s[res[0] : res[1]]
        