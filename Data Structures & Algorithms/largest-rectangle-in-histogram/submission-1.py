class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_height = heights[0]

        for i in range(1, len(heights)):
            ch = heights[i]
            if ch >= stack[-1][1]:
                stack.append((i, ch))
            else:
                start = i
                while len(stack) > 0 and ch < stack[-1][1]:
                    prev = stack.pop()
                    max_height = max(max_height, (i - prev[0]) * prev[1])
                    start = prev[0]
                stack.append((start, ch))

        for item in stack:
            max_height = max(max_height, (len(heights) - item[0]) * item[1])

        return max_height