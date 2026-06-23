class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0

        for n in nums:
            currSum = currSum + n
            maxSum = max(maxSum, currSum)
            currSum = max(currSum, 0)

        return maxSum
