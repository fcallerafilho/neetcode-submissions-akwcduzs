class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            l, r = i, i

            while l >= 0 and heights[l] >= heights[i]:
                l -= 1

            while r < len(heights) and heights[r] >= heights[i]:
                r += 1

            print(heights[i], r, l)
            maxArea = max(maxArea, heights[i]*(r-l-1))
        
        return maxArea


