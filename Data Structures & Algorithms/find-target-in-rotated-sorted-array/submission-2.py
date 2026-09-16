class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        
        return -1