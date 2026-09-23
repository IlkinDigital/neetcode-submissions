class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        aligned = []

        for i in range(len(position)):
            aligned.append((position[i], (target - position[i]) / speed[i]))

        aligned.sort(reverse=True)

        res = len(position)
        prev = aligned[0]
        for i in range(1, len(aligned)):
            if prev[1] >= aligned[i][1]:
                res -= 1
            else:
                prev = aligned[i]

        return res

        # [3, 4, 5, 6, 7, 8]



        
