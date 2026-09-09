class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        starts = []
        for num in num_set:
            if num - 1 not in num_set:
                starts.append(num)

        longest = 0
        for start in starts:
            curr_len = 1
            curr = start
            while curr + 1 in num_set:
                curr_len += 1
                curr += 1
            longest = max(curr_len, longest)
        
        return longest
