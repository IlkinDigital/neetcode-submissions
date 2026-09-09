class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 if num not in freq else freq[num] + 1
        
        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for key, val in freq.items():
            buckets[val].append(key)

        k_freq = []

        for i in range(len(buckets)):
            buck = buckets[len(buckets) - i - 1]
            if len(buck) > 0:
                for num in buck:
                    k_freq.append(num)
                    if len(k_freq) == k:
                        return k_freq

        return k_freq

        