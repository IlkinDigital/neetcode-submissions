class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        l = 1
        r = k

        while l <= r:
            rate = (l + r) // 2
            h_took = 0
            for pile in piles:
                h_took += int(math.ceil(pile / rate))
            
            if h_took <= h:
                r = rate - 1
                k = min(k, rate)
            else:
                l = rate + 1

        return k

        # l = 1
        # r = 1
            