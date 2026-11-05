class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        s, c = [], []

        self.helper(0, nums, target, s, c)
        return s

    def helper(self, i, nums, target, subsets, curr_arr):
        s = sum(curr_arr)
        if s == target:
            subsets.append(curr_arr.copy())
            return
        elif s > target or i >= len(nums):
            return

        curr_arr.append(nums[i])
        self.helper(i, nums, target, subsets, curr_arr)
        curr_arr.pop()
        self.helper(i + 1, nums, target, subsets, curr_arr)