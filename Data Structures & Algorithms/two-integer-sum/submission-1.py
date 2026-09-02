class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {} # num -> index

        for i in range(len(nums)):
            num = nums[i]
            if (target - num) in mem:
                return [mem[target - num], i]
            mem[num] = i

        return []

