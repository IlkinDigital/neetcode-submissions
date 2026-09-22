class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            top = temperatures[s[-1]]
            curr = temperatures[i]

            while top < curr:
                res[s[-1]] = i - s[-1]
                s.pop()
                if len(s) == 0:
                    break
                top = temperatures[s[-1]]
            
            s.append(i)

        return res
