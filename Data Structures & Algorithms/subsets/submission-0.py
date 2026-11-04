class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currSet = [], []

        self.helper(0, nums, subsets, currSet)

        return subsets

    def helper(self, i, nums, subsets, currSet):
        if i >= len(nums):
            subsets.append(currSet.copy())
            return

        currSet.append(nums[i])
        self.helper(i + 1, nums, subsets, currSet)

        currSet.pop()
        self.helper(i + 1, nums, subsets, currSet)