class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(start, end):
            return (end - start) * min(heights[start], heights[end])
        left = 0
        right = len(heights) - 1
        max_area = area(left, right)

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            max_area = max(max_area, area(left, right))

        return max_area