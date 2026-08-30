class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j-i)*min(heights[i], heights[j])
            maxArea = max(maxArea, area)

            if heights[i] >= heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            
        return maxArea