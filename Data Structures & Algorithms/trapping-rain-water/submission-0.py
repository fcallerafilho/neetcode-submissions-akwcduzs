class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0

        for i in range(len(height)):
            rightMax = height[i]
            leftMax = height[i]

            for j in range(0, i):
                leftMax = max(leftMax, height[j])
            for j in range(i, len(height)):
                rightMax = max(rightMax, height[j])
            
            area += min(leftMax, rightMax) - height[i]
        
        return area